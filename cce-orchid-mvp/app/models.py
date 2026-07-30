from __future__ import annotations

import enum
import uuid
from datetime import datetime, timezone
from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, Numeric, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .db import Base


def new_uuid() -> str:
    return str(uuid.uuid4())


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class TenantStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class TenantRole(str, enum.Enum):
    TENANT_ADMIN = "TENANT_ADMIN"


class LocationType(str, enum.Enum):
    SPACE = "SPACE"
    AREA = "AREA"
    RACK = "RACK"
    SHELF = "SHELF"
    SLOT = "SLOT"


class ThingStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    QUARANTINE = "QUARANTINE"
    FOR_SALE = "FOR_SALE"
    RESERVED = "RESERVED"
    TRANSFERRED = "TRANSFERRED"
    ARCHIVED = "ARCHIVED"


class SharingLevel(str, enum.Enum):
    PRIVATE = "PRIVATE"
    TENANT = "TENANT"
    PLATFORM = "PLATFORM"
    SHARED_LINK = "SHARED_LINK"
    PUBLIC = "PUBLIC"


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    identity_uid: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(320), unique=True, nullable=False)
    display_name: Mapped[str] = mapped_column(String(160), nullable=False)
    is_platform_admin: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, nullable=False)

    tenant_links: Mapped[list[UserTenant]] = relationship(back_populates="user", cascade="all, delete-orphan")


class Tenant(Base):
    __tablename__ = "tenants"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    name: Mapped[str] = mapped_column(String(180), nullable=False)
    short_name: Mapped[str] = mapped_column(String(24), nullable=False, unique=True)
    timezone: Mapped[str] = mapped_column(String(80), nullable=False, default="America/Denver")
    default_currency: Mapped[str] = mapped_column(String(3), nullable=False, default="USD")
    status: Mapped[str] = mapped_column(String(20), nullable=False, default=TenantStatus.ACTIVE.value)
    next_accession_sequence: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, nullable=False)

    members: Mapped[list[UserTenant]] = relationship(back_populates="tenant", cascade="all, delete-orphan")
    collections: Mapped[list[Collection]] = relationship(back_populates="tenant", cascade="all, delete-orphan")
    locations: Mapped[list[Location]] = relationship(back_populates="tenant", cascade="all, delete-orphan")
    things: Mapped[list[Thing]] = relationship(back_populates="tenant", cascade="all, delete-orphan")


class UserTenant(Base):
    __tablename__ = "user_tenants"
    __table_args__ = (UniqueConstraint("user_id", "tenant_id", name="uq_user_tenant"),)

    user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    tenant_id: Mapped[str] = mapped_column(ForeignKey("tenants.id", ondelete="CASCADE"), primary_key=True)
    role: Mapped[str] = mapped_column(String(40), nullable=False, default=TenantRole.TENANT_ADMIN.value)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="ACTIVE")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, nullable=False)

    user: Mapped[User] = relationship(back_populates="tenant_links")
    tenant: Mapped[Tenant] = relationship(back_populates="members")


class Collection(Base):
    __tablename__ = "collections"
    __table_args__ = (UniqueConstraint("tenant_id", "name", name="uq_collection_tenant_name"),)

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    tenant_id: Mapped[str] = mapped_column(ForeignKey("tenants.id", ondelete="CASCADE"), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(160), nullable=False)
    template_key: Mapped[str] = mapped_column(String(40), nullable=False, default="ORCHID")
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="ACTIVE")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, nullable=False)

    tenant: Mapped[Tenant] = relationship(back_populates="collections")
    things: Mapped[list[Thing]] = relationship(back_populates="collection")


class Location(Base):
    __tablename__ = "locations"
    __table_args__ = (UniqueConstraint("tenant_id", "parent_id", "name", name="uq_location_path_name"),)

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    tenant_id: Mapped[str] = mapped_column(ForeignKey("tenants.id", ondelete="CASCADE"), nullable=False, index=True)
    parent_id: Mapped[str | None] = mapped_column(ForeignKey("locations.id", ondelete="RESTRICT"), nullable=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    code: Mapped[str | None] = mapped_column(String(40), nullable=True)
    location_type: Mapped[str] = mapped_column(String(20), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, nullable=False)

    tenant: Mapped[Tenant] = relationship(back_populates="locations")
    parent: Mapped[Location | None] = relationship(remote_side=[id], back_populates="children")
    children: Mapped[list[Location]] = relationship(back_populates="parent")
    things: Mapped[list[Thing]] = relationship(back_populates="location")

    @property
    def path(self) -> str:
        parts: list[str] = [self.name]
        node = self.parent
        while node is not None:
            parts.append(node.name)
            node = node.parent
        return " / ".join(reversed(parts))


class Thing(Base):
    __tablename__ = "things"
    __table_args__ = (
        UniqueConstraint("tenant_id", "accession_number", name="uq_thing_accession"),
        UniqueConstraint("label_id", name="uq_thing_label_id"),
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    tenant_id: Mapped[str] = mapped_column(ForeignKey("tenants.id", ondelete="CASCADE"), nullable=False, index=True)
    collection_id: Mapped[str] = mapped_column(ForeignKey("collections.id", ondelete="RESTRICT"), nullable=False)
    location_id: Mapped[str | None] = mapped_column(ForeignKey("locations.id", ondelete="RESTRICT"), nullable=True)
    template_key: Mapped[str] = mapped_column(String(40), nullable=False, default="ORCHID")
    label_id: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    accession_number: Mapped[str] = mapped_column(String(40), nullable=False)
    display_name: Mapped[str] = mapped_column(String(240), nullable=False)
    genus: Mapped[str | None] = mapped_column(String(120), nullable=True)
    species_grex: Mapped[str | None] = mapped_column(String(180), nullable=True)
    cultivar_clone: Mapped[str | None] = mapped_column(String(180), nullable=True)
    narrative: Mapped[str | None] = mapped_column(Text, nullable=True)
    source_name: Mapped[str | None] = mapped_column(String(180), nullable=True)
    acquisition_date: Mapped[str | None] = mapped_column(String(40), nullable=True)
    purchase_price: Mapped[float | None] = mapped_column(Numeric(12, 2), nullable=True)
    currency_code: Mapped[str] = mapped_column(String(3), nullable=False, default="USD")
    status: Mapped[str] = mapped_column(String(30), nullable=False, default=ThingStatus.ACTIVE.value)
    sharing_level: Mapped[str] = mapped_column(String(30), nullable=False, default=SharingLevel.PRIVATE.value)
    created_by_user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="RESTRICT"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, onupdate=utcnow, nullable=False)
    archived_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    tenant: Mapped[Tenant] = relationship(back_populates="things")
    collection: Mapped[Collection] = relationship(back_populates="things")
    location: Mapped[Location | None] = relationship(back_populates="things")
    label_prints: Mapped[list[LabelPrint]] = relationship(back_populates="thing", cascade="all, delete-orphan")


class LabelPrint(Base):
    __tablename__ = "label_prints"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=new_uuid)
    thing_id: Mapped[str] = mapped_column(ForeignKey("things.id", ondelete="CASCADE"), nullable=False, index=True)
    printed_by_user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="RESTRICT"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, nullable=False)

    thing: Mapped[Thing] = relationship(back_populates="label_prints")
