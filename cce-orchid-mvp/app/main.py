from __future__ import annotations

import secrets
from contextlib import asynccontextmanager
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path

try:
    import firebase_admin
    from firebase_admin import auth as firebase_auth
except ImportError:  # Optional for local development; required in production Identity Platform mode.
    firebase_admin = None
    firebase_auth = None
from fastapi import Depends, FastAPI, Form, HTTPException, Request, status
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import func, select
from sqlalchemy.orm import Session, joinedload
from starlette.middleware.sessions import SessionMiddleware

from .auth import get_auth_context, require_platform_admin
from .config import get_settings
from .db import Base, SessionLocal, engine, get_db
from .labels import build_orchid_label_pdf
from .models import Collection, LabelPrint, Location, LocationType, SharingLevel, Tenant, Thing, ThingStatus, User, UserTenant
from .seed import seed_mvp

settings = get_settings()


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as db:
        seed_mvp(db)
    if settings.auth_mode == "identity_platform":
        if firebase_admin is None:
            raise RuntimeError("firebase-admin is required when AUTH_MODE=identity_platform")
        if not firebase_admin._apps:
            firebase_admin.initialize_app()
    yield


app = FastAPI(title="CCE Orchid Enthusiasts MVP", lifespan=lifespan)
app.add_middleware(
    SessionMiddleware,
    secret_key=settings.session_secret,
    same_site="lax",
    https_only=settings.app_env == "production",
    max_age=60 * 60 * 12,
)

BASE_DIR = Path(__file__).resolve().parent
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")
templates.env.globals["settings"] = settings


def redirect_login() -> RedirectResponse:
    return RedirectResponse("/login", status_code=status.HTTP_303_SEE_OTHER)


def current_context(request: Request, db: Session):
    try:
        return get_auth_context(request, db)
    except HTTPException as exc:
        if exc.status_code == 401:
            return None
        raise


def tenant_location_options(db: Session, tenant_id: str) -> list[Location]:
    locations = list(
        db.scalars(
            select(Location)
            .options(joinedload(Location.parent))
            .where(Location.tenant_id == tenant_id, Location.is_active.is_(True))
            .order_by(Location.location_type, Location.name)
        )
    )
    return sorted(locations, key=lambda item: item.path.lower())


def generate_label_id(db: Session) -> str:
    alphabet = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    while True:
        value = "".join(secrets.choice(alphabet) for _ in range(10))
        if not db.scalar(select(Thing.id).where(Thing.label_id == value)):
            return value


def next_accession(db: Session, tenant: Tenant) -> str:
    sequence = tenant.next_accession_sequence
    tenant.next_accession_sequence += 1
    return f"{tenant.short_name}-{datetime.now(timezone.utc).year}-{sequence:04d}"


def parse_price(value: str | None) -> Decimal | None:
    if not value or not value.strip():
        return None
    try:
        return Decimal(value.strip()).quantize(Decimal("0.01"))
    except InvalidOperation as exc:
        raise HTTPException(status_code=422, detail="Purchase price must be a valid number") from exc


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    context = current_context(request, db)
    return templates.TemplateResponse(request, "home.html", {"context": context})


@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse(request, "login.html", {"auth_mode": settings.auth_mode})


@app.post("/auth/dev-login")
def dev_login(request: Request, db: Session = Depends(get_db)):
    if settings.auth_mode != "dev":
        raise HTTPException(status_code=404)
    user = db.scalar(select(User).where(User.email == settings.dev_admin_email))
    if not user:
        raise HTTPException(status_code=500, detail="Seed user missing")
    link = db.scalar(select(UserTenant).where(UserTenant.user_id == user.id, UserTenant.status == "ACTIVE"))
    request.session["user_id"] = user.id
    if link:
        request.session["tenant_id"] = link.tenant_id
    return RedirectResponse("/app", status_code=status.HTTP_303_SEE_OTHER)


@app.post("/auth/session")
async def identity_session(request: Request, db: Session = Depends(get_db)):
    if settings.auth_mode != "identity_platform":
        raise HTTPException(status_code=404)
    payload = await request.json()
    token = payload.get("idToken")
    if not token:
        raise HTTPException(status_code=400, detail="Missing ID token")
    if firebase_auth is None:
        raise HTTPException(status_code=500, detail="Identity Platform support is not installed")
    decoded = firebase_auth.verify_id_token(token)
    identity_uid = decoded["uid"]
    email = decoded.get("email") or f"{identity_uid}@identity.local"
    user = db.scalar(select(User).where(User.identity_uid == identity_uid))
    if not user:
        user = User(identity_uid=identity_uid, email=email, display_name=decoded.get("name") or email)
        db.add(user)
        db.commit()
        db.refresh(user)
    request.session["user_id"] = user.id
    link = db.scalar(select(UserTenant).where(UserTenant.user_id == user.id, UserTenant.status == "ACTIVE"))
    if link:
        request.session["tenant_id"] = link.tenant_id
    return JSONResponse({"ok": True, "redirect": "/app" if link else "/admin/tenants"})


@app.post("/logout")
def logout(request: Request):
    request.session.clear()
    return redirect_login()


@app.get("/app", response_class=HTMLResponse)
def dashboard(request: Request, db: Session = Depends(get_db)):
    context = current_context(request, db)
    if not context:
        return redirect_login()
    tenant_id = context.tenant.id
    counts = {
        "orchids": db.scalar(select(func.count()).select_from(Thing).where(Thing.tenant_id == tenant_id, Thing.archived_at.is_(None))) or 0,
        "locations": db.scalar(select(func.count()).select_from(Location).where(Location.tenant_id == tenant_id, Location.is_active.is_(True))) or 0,
        "unprinted": db.scalar(
            select(func.count()).select_from(Thing).where(
                Thing.tenant_id == tenant_id,
                Thing.archived_at.is_(None),
                ~Thing.label_prints.any(),
            )
        ) or 0,
    }
    recent = list(
        db.scalars(
            select(Thing)
            .options(joinedload(Thing.location))
            .where(Thing.tenant_id == tenant_id)
            .order_by(Thing.created_at.desc())
            .limit(5)
        )
    )
    return templates.TemplateResponse(request, "dashboard.html", {"context": context, "counts": counts, "recent": recent})


@app.get("/admin/tenants", response_class=HTMLResponse)
def admin_tenants(request: Request, db: Session = Depends(get_db)):
    try:
        user = require_platform_admin(request, db)
    except HTTPException as exc:
        if exc.status_code == 401:
            return redirect_login()
        raise
    tenants = list(db.scalars(select(Tenant).order_by(Tenant.name)))
    return templates.TemplateResponse(request, "admin_tenants.html", {"user": user, "tenants": tenants})


@app.post("/admin/tenants")
def create_tenant(
    request: Request,
    name: str = Form(...),
    short_name: str = Form(...),
    admin_email: str = Form(...),
    db: Session = Depends(get_db),
):
    require_platform_admin(request, db)
    short_name = short_name.strip().upper()
    if db.scalar(select(Tenant).where(Tenant.short_name == short_name)):
        raise HTTPException(status_code=409, detail="Tenant short name already exists")
    tenant = Tenant(name=name.strip(), short_name=short_name, timezone=settings.default_timezone, default_currency=settings.default_currency)
    db.add(tenant)
    db.flush()
    user = db.scalar(select(User).where(User.email == admin_email.strip().lower()))
    if not user:
        user = User(identity_uid=f"pending:{admin_email.strip().lower()}", email=admin_email.strip().lower(), display_name=admin_email.strip())
        db.add(user)
        db.flush()
    db.add(UserTenant(user_id=user.id, tenant_id=tenant.id, role="TENANT_ADMIN"))
    db.add(Collection(tenant_id=tenant.id, name="Main Orchid Collection", template_key="ORCHID"))
    db.commit()
    return RedirectResponse("/admin/tenants", status_code=status.HTTP_303_SEE_OTHER)


@app.post("/tenant/select/{tenant_id}")
def select_tenant(tenant_id: str, request: Request, db: Session = Depends(get_db)):
    user_id = request.session.get("user_id")
    link = db.scalar(select(UserTenant).where(UserTenant.user_id == user_id, UserTenant.tenant_id == tenant_id, UserTenant.status == "ACTIVE"))
    if not link:
        raise HTTPException(status_code=403)
    request.session["tenant_id"] = tenant_id
    return RedirectResponse("/app", status_code=status.HTTP_303_SEE_OTHER)


@app.get("/locations", response_class=HTMLResponse)
def locations_page(request: Request, db: Session = Depends(get_db)):
    context = current_context(request, db)
    if not context:
        return redirect_login()
    locations = tenant_location_options(db, context.tenant.id)
    return templates.TemplateResponse(
        request,
        "locations.html",
        {"context": context, "locations": locations, "location_types": [item.value for item in LocationType]},
    )


@app.post("/locations")
def create_location(
    request: Request,
    name: str = Form(...),
    location_type: str = Form(...),
    parent_id: str = Form(""),
    code: str = Form(""),
    db: Session = Depends(get_db),
):
    context = get_auth_context(request, db)
    if location_type not in {item.value for item in LocationType}:
        raise HTTPException(status_code=422, detail="Invalid location type")
    parent = None
    if parent_id:
        parent = db.get(Location, parent_id)
        if not parent or parent.tenant_id != context.tenant.id:
            raise HTTPException(status_code=422, detail="Invalid parent location")
    location = Location(
        tenant_id=context.tenant.id,
        parent_id=parent.id if parent else None,
        name=name.strip(),
        code=code.strip() or None,
        location_type=location_type,
    )
    db.add(location)
    db.commit()
    return RedirectResponse("/locations", status_code=status.HTTP_303_SEE_OTHER)


@app.post("/locations/{location_id}/toggle")
def toggle_location(location_id: str, request: Request, db: Session = Depends(get_db)):
    context = get_auth_context(request, db)
    location = db.get(Location, location_id)
    if not location or location.tenant_id != context.tenant.id:
        raise HTTPException(status_code=404)
    location.is_active = not location.is_active
    db.commit()
    return RedirectResponse("/locations", status_code=status.HTTP_303_SEE_OTHER)


@app.get("/orchids", response_class=HTMLResponse)
def orchid_list(request: Request, db: Session = Depends(get_db)):
    context = current_context(request, db)
    if not context:
        return redirect_login()
    orchids = list(
        db.scalars(
            select(Thing)
            .options(joinedload(Thing.location), joinedload(Thing.collection), joinedload(Thing.label_prints))
            .where(Thing.tenant_id == context.tenant.id)
            .order_by(Thing.archived_at.is_not(None), Thing.display_name)
        ).unique()
    )
    return templates.TemplateResponse(request, "orchid_list.html", {"context": context, "orchids": orchids})


@app.get("/orchids/new", response_class=HTMLResponse)
def orchid_new(request: Request, db: Session = Depends(get_db)):
    context = current_context(request, db)
    if not context:
        return redirect_login()
    collections = list(db.scalars(select(Collection).where(Collection.tenant_id == context.tenant.id, Collection.status == "ACTIVE")))
    locations = tenant_location_options(db, context.tenant.id)
    return templates.TemplateResponse(
        request,
        "orchid_form.html",
        {
            "context": context,
            "orchid": None,
            "collections": collections,
            "locations": locations,
            "statuses": [item.value for item in ThingStatus if item != ThingStatus.ARCHIVED],
            "action": "/orchids",
            "title": "Add Orchid",
        },
    )


@app.post("/orchids")
def orchid_create(
    request: Request,
    display_name: str = Form(...),
    collection_id: str = Form(...),
    location_id: str = Form(""),
    status_value: str = Form(ThingStatus.ACTIVE.value, alias="status"),
    genus: str = Form(""),
    species_grex: str = Form(""),
    cultivar_clone: str = Form(""),
    narrative: str = Form(""),
    source_name: str = Form(""),
    acquisition_date: str = Form(""),
    purchase_price: str = Form(""),
    db: Session = Depends(get_db),
):
    context = get_auth_context(request, db)
    collection = db.get(Collection, collection_id)
    if not collection or collection.tenant_id != context.tenant.id:
        raise HTTPException(status_code=422, detail="Invalid collection")
    location = None
    if location_id:
        location = db.get(Location, location_id)
        if not location or location.tenant_id != context.tenant.id or not location.is_active:
            raise HTTPException(status_code=422, detail="Invalid location")
    if status_value not in {item.value for item in ThingStatus if item != ThingStatus.ARCHIVED}:
        raise HTTPException(status_code=422, detail="Invalid status")
    thing = Thing(
        tenant_id=context.tenant.id,
        collection_id=collection.id,
        location_id=location.id if location else None,
        label_id=generate_label_id(db),
        accession_number=next_accession(db, context.tenant),
        display_name=display_name.strip(),
        genus=genus.strip() or None,
        species_grex=species_grex.strip() or None,
        cultivar_clone=cultivar_clone.strip() or None,
        narrative=narrative.strip() or None,
        source_name=source_name.strip() or None,
        acquisition_date=acquisition_date.strip() or None,
        purchase_price=parse_price(purchase_price),
        currency_code=context.tenant.default_currency,
        status=status_value,
        sharing_level=SharingLevel.PRIVATE.value,
        created_by_user_id=context.user.id,
    )
    db.add(thing)
    db.commit()
    db.refresh(thing)
    return RedirectResponse(f"/orchids/{thing.id}", status_code=status.HTTP_303_SEE_OTHER)


@app.get("/orchids/{thing_id}", response_class=HTMLResponse)
def orchid_detail(thing_id: str, request: Request, db: Session = Depends(get_db)):
    context = current_context(request, db)
    if not context:
        return redirect_login()
    orchid = db.scalar(
        select(Thing)
        .options(joinedload(Thing.location), joinedload(Thing.collection), joinedload(Thing.label_prints))
        .where(Thing.id == thing_id, Thing.tenant_id == context.tenant.id)
    )
    if not orchid:
        raise HTTPException(status_code=404)
    return templates.TemplateResponse(request, "orchid_detail.html", {"context": context, "orchid": orchid})


@app.get("/orchids/{thing_id}/edit", response_class=HTMLResponse)
def orchid_edit(thing_id: str, request: Request, db: Session = Depends(get_db)):
    context = current_context(request, db)
    if not context:
        return redirect_login()
    orchid = db.get(Thing, thing_id)
    if not orchid or orchid.tenant_id != context.tenant.id:
        raise HTTPException(status_code=404)
    collections = list(db.scalars(select(Collection).where(Collection.tenant_id == context.tenant.id, Collection.status == "ACTIVE")))
    locations = tenant_location_options(db, context.tenant.id)
    return templates.TemplateResponse(
        request,
        "orchid_form.html",
        {
            "context": context,
            "orchid": orchid,
            "collections": collections,
            "locations": locations,
            "statuses": [item.value for item in ThingStatus if item != ThingStatus.ARCHIVED],
            "action": f"/orchids/{orchid.id}",
            "title": "Edit Orchid",
        },
    )


@app.post("/orchids/{thing_id}")
def orchid_update(
    thing_id: str,
    request: Request,
    display_name: str = Form(...),
    collection_id: str = Form(...),
    location_id: str = Form(""),
    status_value: str = Form(ThingStatus.ACTIVE.value, alias="status"),
    genus: str = Form(""),
    species_grex: str = Form(""),
    cultivar_clone: str = Form(""),
    narrative: str = Form(""),
    source_name: str = Form(""),
    acquisition_date: str = Form(""),
    purchase_price: str = Form(""),
    db: Session = Depends(get_db),
):
    context = get_auth_context(request, db)
    orchid = db.get(Thing, thing_id)
    if not orchid or orchid.tenant_id != context.tenant.id:
        raise HTTPException(status_code=404)
    collection = db.get(Collection, collection_id)
    if not collection or collection.tenant_id != context.tenant.id:
        raise HTTPException(status_code=422, detail="Invalid collection")
    location = None
    if location_id:
        location = db.get(Location, location_id)
        if not location or location.tenant_id != context.tenant.id or not location.is_active:
            raise HTTPException(status_code=422, detail="Invalid location")
    orchid.display_name = display_name.strip()
    orchid.collection_id = collection.id
    orchid.location_id = location.id if location else None
    orchid.status = status_value
    orchid.genus = genus.strip() or None
    orchid.species_grex = species_grex.strip() or None
    orchid.cultivar_clone = cultivar_clone.strip() or None
    orchid.narrative = narrative.strip() or None
    orchid.source_name = source_name.strip() or None
    orchid.acquisition_date = acquisition_date.strip() or None
    orchid.purchase_price = parse_price(purchase_price)
    db.commit()
    return RedirectResponse(f"/orchids/{orchid.id}", status_code=status.HTTP_303_SEE_OTHER)


@app.post("/orchids/{thing_id}/archive")
def orchid_archive(thing_id: str, request: Request, db: Session = Depends(get_db)):
    context = get_auth_context(request, db)
    orchid = db.get(Thing, thing_id)
    if not orchid or orchid.tenant_id != context.tenant.id:
        raise HTTPException(status_code=404)
    orchid.status = ThingStatus.ARCHIVED.value
    orchid.archived_at = datetime.now(timezone.utc)
    db.commit()
    return RedirectResponse(f"/orchids/{orchid.id}", status_code=status.HTTP_303_SEE_OTHER)


@app.post("/orchids/{thing_id}/restore")
def orchid_restore(thing_id: str, request: Request, db: Session = Depends(get_db)):
    context = get_auth_context(request, db)
    orchid = db.get(Thing, thing_id)
    if not orchid or orchid.tenant_id != context.tenant.id:
        raise HTTPException(status_code=404)
    orchid.status = ThingStatus.ACTIVE.value
    orchid.archived_at = None
    db.commit()
    return RedirectResponse(f"/orchids/{orchid.id}", status_code=status.HTTP_303_SEE_OTHER)


@app.get("/orchids/{thing_id}/label.pdf")
def orchid_label(thing_id: str, request: Request, db: Session = Depends(get_db)):
    context = get_auth_context(request, db)
    orchid = db.scalar(select(Thing).options(joinedload(Thing.location)).where(Thing.id == thing_id, Thing.tenant_id == context.tenant.id))
    if not orchid:
        raise HTTPException(status_code=404)
    pdf = build_orchid_label_pdf(orchid, settings.public_base_url)
    db.add(LabelPrint(thing_id=orchid.id, printed_by_user_id=context.user.id))
    db.commit()
    filename = f"{orchid.accession_number}-label.pdf"
    return Response(pdf, media_type="application/pdf", headers={"Content-Disposition": f'inline; filename="{filename}"'})


@app.get("/p/{label_id}", response_class=HTMLResponse)
def public_label_lookup(label_id: str, request: Request, db: Session = Depends(get_db)):
    orchid = db.scalar(
        select(Thing)
        .options(joinedload(Thing.location), joinedload(Thing.collection), joinedload(Thing.tenant))
        .where(Thing.label_id == label_id)
    )
    if not orchid:
        raise HTTPException(status_code=404)
    authorized = False
    user_id = request.session.get("user_id")
    if user_id:
        authorized = bool(db.scalar(select(UserTenant).where(UserTenant.user_id == user_id, UserTenant.tenant_id == orchid.tenant_id, UserTenant.status == "ACTIVE")))
    is_shared = orchid.sharing_level in {SharingLevel.PUBLIC.value, SharingLevel.PLATFORM.value, SharingLevel.SHARED_LINK.value}
    return templates.TemplateResponse(request, "public_orchid.html", {"orchid": orchid, "authorized": authorized, "is_shared": is_shared})
