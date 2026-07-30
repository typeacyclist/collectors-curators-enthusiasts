from __future__ import annotations

from dataclasses import dataclass
from fastapi import HTTPException, Request, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from .models import Tenant, User, UserTenant


@dataclass
class AuthContext:
    user: User
    tenant: Tenant | None
    tenant_role: str | None


def get_auth_context(request: Request, db: Session, require_tenant: bool = True) -> AuthContext:
    user_id = request.session.get("user_id")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Sign in required")

    user = db.get(User, user_id)
    if not user:
        request.session.clear()
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid session")

    tenant_id = request.session.get("tenant_id")
    if not tenant_id:
        if require_tenant:
            link = db.scalar(
                select(UserTenant).where(
                    UserTenant.user_id == user.id,
                    UserTenant.status == "ACTIVE",
                )
            )
            if not link:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No active tenant")
            tenant_id = link.tenant_id
            request.session["tenant_id"] = tenant_id
        else:
            return AuthContext(user=user, tenant=None, tenant_role=None)

    link = db.scalar(
        select(UserTenant).where(
            UserTenant.user_id == user.id,
            UserTenant.tenant_id == tenant_id,
            UserTenant.status == "ACTIVE",
        )
    )
    if not link:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Tenant access denied")

    tenant = db.get(Tenant, tenant_id)
    if not tenant or tenant.status != "ACTIVE":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Tenant unavailable")

    return AuthContext(user=user, tenant=tenant, tenant_role=link.role)


def require_platform_admin(request: Request, db: Session) -> User:
    context = get_auth_context(request, db, require_tenant=False)
    if not context.user.is_platform_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Platform administrator required")
    return context.user
