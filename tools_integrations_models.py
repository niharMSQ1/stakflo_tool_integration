"""
ORM models for tools/integrations: tools, controls, evidence_masters, and link tables.

Column types and constraints match `stakflo_models.py` (same PostgreSQL schema).
"""
from __future__ import annotations

import datetime as dt
from typing import Any
from uuid import UUID

from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSON, UUID as PGUUID


class Base(DeclarativeBase):
    pass


class Tools(Base):
    """Integration/tool catalog (referenced by `evidence_masters.tool_id`)."""

    __tablename__ = "tools"
    __table_args__ = (UniqueConstraint("name", name="tools_name_unique"),)

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True)
    name: Mapped[str | None] = mapped_column(String(255))
    image_path: Mapped[str | None] = mapped_column(String(255))
    configuration_keys: Mapped[Any | None] = mapped_column(JSON())
    status: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str | None] = mapped_column(String(255))
    sync_type: Mapped[str | None] = mapped_column(String())
    scope: Mapped[Any | None] = mapped_column(JSON())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())


class Controls(Base):
    """Canonical control catalog (framework-level control definitions)."""

    __tablename__ = "controls"
    __table_args__ = (UniqueConstraint("short_name", name="controls_short_name_unique"),)

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True)
    short_name: Mapped[str] = mapped_column(String(255), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(), nullable=False)
    category: Mapped[str | None] = mapped_column(String(255))
    level: Mapped[int | None] = mapped_column(Integer())
    group: Mapped[str | None] = mapped_column(String(255))
    frequency: Mapped[str | None] = mapped_column(String(255))
    is_active: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())


class EvidenceMasters(Base):
    """Catalog of evidence types (often tied to a tool/integration via `tool_id`)."""

    __tablename__ = "evidence_masters"
    __table_args__ = (UniqueConstraint("code", name="evidence_masters_code_unique"),)

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True)
    tool_id: Mapped[UUID | None] = mapped_column(PGUUID(as_uuid=True), ForeignKey("tools.id"))
    category: Mapped[str | None] = mapped_column(String(100))
    code: Mapped[str] = mapped_column(String(50), nullable=False)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    evidence_type: Mapped[str | None] = mapped_column(String(50))
    source: Mapped[str | None] = mapped_column(String(100))
    api_endpoint: Mapped[str | None] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(String())
    expected_frequency: Mapped[str | None] = mapped_column(String(50))
    is_required_evidence: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())


class ControlEvidenceMaster(Base):
    """Many-to-many: which evidence master rows apply to which controls."""

    __tablename__ = "control_evidence_master"

    control_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("controls.id"), primary_key=True
    )
    evidence_master_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("evidence_masters.id"), primary_key=True
    )
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
