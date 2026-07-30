from sqlalchemy import select
from sqlalchemy.orm import Session
from .config import get_settings
from .models import Collection, Location, Tenant, User, UserTenant


def seed_mvp(db: Session) -> None:
    settings = get_settings()
    user = db.scalar(select(User).where(User.email == settings.dev_admin_email))
    if not user:
        user = User(
            identity_uid=f"dev:{settings.dev_admin_email}",
            email=settings.dev_admin_email,
            display_name=settings.dev_admin_name,
            is_platform_admin=True,
        )
        db.add(user)
        db.flush()

    tenant = db.scalar(select(Tenant).where(Tenant.short_name == settings.default_tenant_short_name))
    if not tenant:
        tenant = Tenant(
            name=settings.default_tenant_name,
            short_name=settings.default_tenant_short_name,
            timezone=settings.default_timezone,
            default_currency=settings.default_currency,
        )
        db.add(tenant)
        db.flush()

    link = db.scalar(select(UserTenant).where(UserTenant.user_id == user.id, UserTenant.tenant_id == tenant.id))
    if not link:
        db.add(UserTenant(user_id=user.id, tenant_id=tenant.id, role="TENANT_ADMIN"))

    collection = db.scalar(select(Collection).where(Collection.tenant_id == tenant.id, Collection.name == "Main Orchid Collection"))
    if not collection:
        db.add(Collection(tenant_id=tenant.id, name="Main Orchid Collection", template_key="ORCHID"))

    root = db.scalar(select(Location).where(Location.tenant_id == tenant.id, Location.name == "PCO Growing Facility"))
    if not root:
        root = Location(tenant_id=tenant.id, name="PCO Growing Facility", code="PCO", location_type="SPACE")
        db.add(root)
        db.flush()
        area = Location(tenant_id=tenant.id, parent_id=root.id, name="Main Growing Area", code="MAIN", location_type="AREA")
        db.add(area)
        db.flush()
        rack = Location(tenant_id=tenant.id, parent_id=area.id, name="Rack 1", code="R1", location_type="RACK")
        db.add(rack)
        db.flush()
        db.add_all([
            Location(tenant_id=tenant.id, parent_id=rack.id, name="Shelf 1", code="S1", location_type="SHELF"),
            Location(tenant_id=tenant.id, parent_id=rack.id, name="Shelf 2", code="S2", location_type="SHELF"),
            Location(tenant_id=tenant.id, parent_id=root.id, name="Quarantine Area", code="Q", location_type="AREA"),
        ])

    db.commit()
