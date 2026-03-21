"""
SQLAlchemy ORM models reflected from PostgreSQL.
Regenerate: python ignored_folder/generate_models.py
"""
from __future__ import annotations

import datetime as dt
from typing import Any
from uuid import UUID

from sqlalchemy import (
    ARRAY,
    BigInteger,
    Boolean,
    Date,
    DateTime,
    Float,
    ForeignKey,
    ForeignKeyConstraint,
    Integer,
    Interval,
    LargeBinary,
    Numeric,
    SmallInteger,
    String,
    Text,
    Time,
    UniqueConstraint,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import (

    BYTEA,

    CIDR,

    ENUM,

    HSTORE,

    INET,

    JSON,

    JSONB,

    TSVECTOR,

    UUID,

)


class Base(DeclarativeBase):
    pass

class Assets(Base):
    __tablename__ = 'assets'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    organization_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('organizations.id'), nullable=False)
    platform: Mapped[str | None] = mapped_column(String(255))
    scope: Mapped[str | None] = mapped_column(String(255))
    name: Mapped[str | None] = mapped_column(String(255))
    host_name: Mapped[str | None] = mapped_column(String(255))
    os_name: Mapped[str | None] = mapped_column(String(255))
    os_version: Mapped[str | None] = mapped_column(String(255))
    ip_address: Mapped[str | None] = mapped_column(String(255))
    port: Mapped[str | None] = mapped_column(String(255))
    protocol: Mapped[str | None] = mapped_column(String(255))
    type: Mapped[str | None] = mapped_column(String(255))
    tags: Mapped[str | None] = mapped_column(String(255))
    agent_check_in: Mapped[str | None] = mapped_column(String(255))
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class AuditClauseStatuses(Base):
    __tablename__ = 'audit_clause_statuses'
    __table_args__ = (UniqueConstraint('audit_id', 'clause_id', name='audit_clause_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    audit_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('audits.id'), nullable=False)
    clause_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('clauses.id'), nullable=False)
    status: Mapped[str] = mapped_column(String(255), nullable=False)
    auditor_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id'))
    remarks: Mapped[str | None] = mapped_column(String())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class AuditMappings(Base):
    __tablename__ = 'audit_mappings'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    audit_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('audits.id'), nullable=False)
    auditable_type: Mapped[str] = mapped_column(String(255), nullable=False)
    auditable_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class Auditors(Base):
    __tablename__ = 'auditors'
    __table_args__ = (UniqueConstraint('organization_id', 'email', name='auditors_organization_id_email_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    name: Mapped[str | None] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    organization_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('organizations.id'), nullable=False)
    password: Mapped[str | None] = mapped_column(String(255))
    status: Mapped[str | None] = mapped_column(String(255))
    remember_token: Mapped[str | None] = mapped_column(String(100))
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class Audits(Base):
    __tablename__ = 'audits'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    organization_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('organizations.id'), nullable=False)
    audit_type: Mapped[str] = mapped_column(String(255), nullable=False)
    audit_title: Mapped[str] = mapped_column(String(255), nullable=False)
    framework_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('certificates.id'), nullable=False)
    start_date: Mapped[dt.date] = mapped_column(Date(), nullable=False)
    end_date: Mapped[dt.date] = mapped_column(Date(), nullable=False)
    poc_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    auditor_organization: Mapped[str | None] = mapped_column(String(255))
    scope_details: Mapped[Any | None] = mapped_column(JSONB())
    status: Mapped[str] = mapped_column(String(255), nullable=False)
    access_start_date: Mapped[dt.date | None] = mapped_column(Date())
    access_end_date: Mapped[dt.date | None] = mapped_column(Date())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class BasicSettings(Base):
    __tablename__ = 'basic_settings'
    __table_args__ = (UniqueConstraint('organization_id', name='basic_settings_organization_id_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    organization_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('organizations.id'))
    language: Mapped[str] = mapped_column(String(10), nullable=False)
    timezone: Mapped[str] = mapped_column(String(100), nullable=False)
    date_format: Mapped[str] = mapped_column(String(20), nullable=False)
    time_format: Mapped[str] = mapped_column(String(20), nullable=False)
    number_format: Mapped[str] = mapped_column(String(10), nullable=False)
    currency: Mapped[str] = mapped_column(String(10), nullable=False)
    currency_symbol: Mapped[str] = mapped_column(String(10), nullable=False)
    theme_mode: Mapped[str] = mapped_column(String(10), nullable=False)
    default_landing_page: Mapped[str | None] = mapped_column(String(100))
    maintenance_mode: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class Cache(Base):
    __tablename__ = 'cache'
    key: Mapped[str] = mapped_column(String(255), primary_key=True)
    value: Mapped[str] = mapped_column(String(), nullable=False)
    expiration: Mapped[int] = mapped_column(Integer(), nullable=False)

class CacheLocks(Base):
    __tablename__ = 'cache_locks'
    key: Mapped[str] = mapped_column(String(255), primary_key=True)
    owner: Mapped[str] = mapped_column(String(255), nullable=False)
    expiration: Mapped[int] = mapped_column(Integer(), nullable=False)

class Categories(Base):
    __tablename__ = 'categories'
    __table_args__ = (UniqueConstraint('name', name='categories_name_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(String())
    status: Mapped[str | None] = mapped_column(String())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class CertificateDrafts(Base):
    __tablename__ = 'certificate_drafts'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(String())
    image_url: Mapped[str | None] = mapped_column(String(255))
    url: Mapped[str | None] = mapped_column(String(255))
    primary_domain: Mapped[str | None] = mapped_column(String(255))
    secondary_domain: Mapped[str | None] = mapped_column(String(255))
    labels: Mapped[Any | None] = mapped_column(JSON())
    category: Mapped[str | None] = mapped_column(String(255))
    created_by: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True))
    organization_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True))
    is_published: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    published_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class CertificateProviders(Base):
    __tablename__ = 'certificate_providers'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class Certificates(Base):
    __tablename__ = 'certificates'
    __table_args__ = (UniqueConstraint('name', name='certificates_name_unique'), UniqueConstraint('slug', name='certificates_slug_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(String())
    image_url: Mapped[str | None] = mapped_column(String(255))
    url: Mapped[str | None] = mapped_column(String(255))
    primary_domain: Mapped[str | None] = mapped_column(String(255))
    secondary_domain: Mapped[str | None] = mapped_column(String(255))
    labels: Mapped[Any | None] = mapped_column(JSON())
    category: Mapped[str | None] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class Clauses(Base):
    __tablename__ = 'clauses'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    certificate_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('certificates.id'), nullable=False)
    reference_id: Mapped[str] = mapped_column(String(255), nullable=False)
    display_identifier: Mapped[str] = mapped_column(String(255), nullable=False)
    title: Mapped[str | None] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(String())
    parent_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('clauses.id'))
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class Comments(Base):
    __tablename__ = 'comments'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    user_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    comment: Mapped[str] = mapped_column(String(), nullable=False)
    commentable_type: Mapped[str] = mapped_column(String(255), nullable=False)
    commentable_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class ControlClauses(Base):
    __tablename__ = 'control_clauses'
    __table_args__ = (UniqueConstraint('control_id', 'clause_id', name='control_clauses_control_id_clause_id_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    control_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('controls.id'), nullable=False)
    clause_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('clauses.id'), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class ControlEvidenceMaster(Base):
    __tablename__ = 'control_evidence_master'
    control_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('controls.id'), primary_key=True)
    evidence_master_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('evidence_masters.id'), primary_key=True)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class ControlScenarios(Base):
    __tablename__ = 'control_scenarios'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    control_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('controls.id'), nullable=False)
    tool_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('tools.id'), nullable=False)
    evidence_name: Mapped[str] = mapped_column(String(255), nullable=False)
    evidence_type: Mapped[str | None] = mapped_column(String(50))
    action: Mapped[str | None] = mapped_column(String(100))
    actions: Mapped[Any | None] = mapped_column(JSON())
    description: Mapped[str | None] = mapped_column(String())
    status: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class Controls(Base):
    __tablename__ = 'controls'
    __table_args__ = (UniqueConstraint('short_name', name='controls_short_name_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
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

class Countries(Base):
    __tablename__ = 'countries'
    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    iso3: Mapped[str] = mapped_column(String(255), nullable=False)
    iso2: Mapped[str] = mapped_column(String(255), nullable=False)
    phonecode: Mapped[str] = mapped_column(String(255), nullable=False)
    capital: Mapped[str] = mapped_column(String(255), nullable=False)
    currency: Mapped[str] = mapped_column(String(255), nullable=False)
    currency_symbol: Mapped[str] = mapped_column(String(255), nullable=False)
    tld: Mapped[str] = mapped_column(String(255), nullable=False)
    native: Mapped[str | None] = mapped_column(String(255))
    region: Mapped[str] = mapped_column(String(255), nullable=False)
    subregion: Mapped[str] = mapped_column(String(255), nullable=False)
    timezones: Mapped[str] = mapped_column(String(), nullable=False)
    translations: Mapped[str | None] = mapped_column(String())
    latitude: Mapped[str] = mapped_column(String(), nullable=False)
    longitude: Mapped[str] = mapped_column(String(), nullable=False)
    emoji: Mapped[str] = mapped_column(String(), nullable=False)
    emojiU: Mapped[str] = mapped_column(String(), nullable=False)
    flag: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    wikiDataId: Mapped[str | None] = mapped_column(String())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class DataSubjectRequests(Base):
    __tablename__ = 'data_subject_requests'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    organization_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('organizations.id'))
    organization_name: Mapped[str | None] = mapped_column(String(255))
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    phone: Mapped[str | None] = mapped_column(String(255))
    country: Mapped[str | None] = mapped_column(String(255))
    relationship_with: Mapped[str | None] = mapped_column(String(255))
    if_other_relationship: Mapped[str | None] = mapped_column(String(255))
    request_type: Mapped[str] = mapped_column(String(255), nullable=False)
    request_details: Mapped[str | None] = mapped_column(String())
    file_path: Mapped[str | None] = mapped_column(String(255))
    identity_verified: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    identity_verified_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    status: Mapped[str] = mapped_column(String(255), nullable=False)
    requested_date: Mapped[dt.date] = mapped_column(Date(), nullable=False)
    assigned_to: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id'))
    assigned_date: Mapped[dt.date | None] = mapped_column(Date())
    due_date: Mapped[dt.date | None] = mapped_column(Date())
    completed_date: Mapped[dt.date | None] = mapped_column(Date())
    rejection_reason: Mapped[str | None] = mapped_column(String())
    internal_notes: Mapped[str | None] = mapped_column(String())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    deleted_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class EmailLogs(Base):
    __tablename__ = 'email_logs'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    organization_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('organizations.id'))
    to_email: Mapped[str] = mapped_column(String(255), nullable=False)
    subject: Mapped[str | None] = mapped_column(String(255))
    mailable: Mapped[str | None] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(255), nullable=False)
    error_message: Mapped[str | None] = mapped_column(String())
    emailable_type: Mapped[str | None] = mapped_column(String(255))
    emailable_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True))
    queued_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    sent_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    failed_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class Employees(Base):
    __tablename__ = 'employees'
    __table_args__ = (UniqueConstraint('organization_id', 'email', name='employees_organization_id_email_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    organization_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('organizations.id'), nullable=False)
    sync_user_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id'))
    department: Mapped[str | None] = mapped_column(String(255))
    designation: Mapped[str | None] = mapped_column(String(255))
    name: Mapped[str | None] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    password: Mapped[str | None] = mapped_column(String(255))
    image: Mapped[str | None] = mapped_column(String(255))
    provider: Mapped[str | None] = mapped_column(String(255))
    provider_id: Mapped[str | None] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(255), nullable=False)
    reg_status: Mapped[str | None] = mapped_column(String(255))
    mode: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    employee_status: Mapped[str | None] = mapped_column(String(255))
    remember_token: Mapped[str | None] = mapped_column(String(100))
    has_changed: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    changed_values: Mapped[str | None] = mapped_column(String(255))
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class Evidence(Base):
    __tablename__ = 'evidence'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    organization_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('organizations.id'), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    code: Mapped[str | None] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(String())
    due_date: Mapped[dt.date | None] = mapped_column(Date())
    status: Mapped[str | None] = mapped_column(String(255))
    tool_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('tools.id'))
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class EvidenceCollections(Base):
    __tablename__ = 'evidence_collections'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    evidence_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('evidence.id'), nullable=False)
    evidence_from: Mapped[str | None] = mapped_column(String(255))
    source: Mapped[str | None] = mapped_column(String(255))
    name: Mapped[str | None] = mapped_column(String(255))
    tool_evidence: Mapped[Any | None] = mapped_column(JSONB())
    updated_by: Mapped[str | None] = mapped_column(String(255))
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class EvidenceMappeds(Base):
    __tablename__ = 'evidence_mappeds'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    evidence_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('evidence.id'), nullable=False)
    evidenceable_type: Mapped[str] = mapped_column(String(255), nullable=False)
    evidenceable_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    mapped_by: Mapped[str | None] = mapped_column(String(255))
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class EvidenceMasters(Base):
    __tablename__ = 'evidence_masters'
    __table_args__ = (UniqueConstraint('code', name='evidence_masters_code_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    tool_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('tools.id'))
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

class FailedJobs(Base):
    __tablename__ = 'failed_jobs'
    __table_args__ = (UniqueConstraint('uuid', name='failed_jobs_uuid_unique'),)
    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)
    uuid: Mapped[str] = mapped_column(String(255), nullable=False)
    connection: Mapped[str] = mapped_column(String(), nullable=False)
    queue: Mapped[str] = mapped_column(String(), nullable=False)
    payload: Mapped[str] = mapped_column(String(), nullable=False)
    exception: Mapped[str] = mapped_column(String(), nullable=False)
    failed_at: Mapped[dt.datetime] = mapped_column(DateTime(), nullable=False)

class FrameworkImportDrafts(Base):
    __tablename__ = 'framework_import_drafts'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    organization_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('organizations.id'), nullable=False)
    certificate_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('certificates.id'))
    import_data: Mapped[Any] = mapped_column(JSON(), nullable=False)
    status: Mapped[str] = mapped_column(String(255), nullable=False)
    created_by: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id'))
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    certificate_draft_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('certificate_drafts.id'))

class Frameworks(Base):
    __tablename__ = 'frameworks'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class IntegrationData(Base):
    __tablename__ = 'integration_data'
    __table_args__ = (UniqueConstraint('platform', 'external_id', 'organization_id', name='unique_platform_external_org'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    organization_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('organizations.id'), nullable=False)
    platform: Mapped[str | None] = mapped_column(String(50))
    scope: Mapped[str | None] = mapped_column(String(50))
    external_id: Mapped[str | None] = mapped_column(String(255))
    data: Mapped[Any | None] = mapped_column(JSON())
    fetched_at: Mapped[dt.datetime] = mapped_column(DateTime(), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class InternalControls(Base):
    __tablename__ = 'internal_controls'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    control_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('controls.id'), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(String())
    frequency: Mapped[str | None] = mapped_column(String(255))
    owner_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id'))
    evidence_required: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    status: Mapped[str] = mapped_column(String(255), nullable=False)
    metadata: Mapped[Any | None] = mapped_column(JSON())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class JobBatches(Base):
    __tablename__ = 'job_batches'
    id: Mapped[str] = mapped_column(String(255), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    total_jobs: Mapped[int] = mapped_column(Integer(), nullable=False)
    pending_jobs: Mapped[int] = mapped_column(Integer(), nullable=False)
    failed_jobs: Mapped[int] = mapped_column(Integer(), nullable=False)
    failed_job_ids: Mapped[str] = mapped_column(String(), nullable=False)
    options: Mapped[str | None] = mapped_column(String())
    cancelled_at: Mapped[int | None] = mapped_column(Integer())
    created_at: Mapped[int] = mapped_column(Integer(), nullable=False)
    finished_at: Mapped[int | None] = mapped_column(Integer())

class Jobs(Base):
    __tablename__ = 'jobs'
    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)
    queue: Mapped[str] = mapped_column(String(255), nullable=False)
    payload: Mapped[str] = mapped_column(String(), nullable=False)
    attempts: Mapped[int] = mapped_column(Integer(), nullable=False)
    reserved_at: Mapped[int | None] = mapped_column(Integer())
    available_at: Mapped[int] = mapped_column(Integer(), nullable=False)
    created_at: Mapped[int] = mapped_column(Integer(), nullable=False)

class Migrations(Base):
    __tablename__ = 'migrations'
    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)
    migration: Mapped[str] = mapped_column(String(255), nullable=False)
    batch: Mapped[int] = mapped_column(Integer(), nullable=False)

class Notifications(Base):
    __tablename__ = 'notifications'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    notifiable_type: Mapped[str] = mapped_column(String(255), nullable=False)
    notifiable_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    organization_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('organizations.id'), nullable=False)
    message: Mapped[str | None] = mapped_column(String())
    data: Mapped[Any | None] = mapped_column(JSON())
    type: Mapped[str] = mapped_column(String(255), nullable=False)
    read_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class OauthAccessTokens(Base):
    __tablename__ = 'oauth_access_tokens'
    id: Mapped[str] = mapped_column(String(80), primary_key=True)
    user_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True))
    client_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    name: Mapped[str | None] = mapped_column(String(255))
    scopes: Mapped[str | None] = mapped_column(String())
    revoked: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    expires_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class OauthClients(Base):
    __tablename__ = 'oauth_clients'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    owner_type: Mapped[str | None] = mapped_column(String(255))
    owner_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True))
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    secret: Mapped[str | None] = mapped_column(String(255))
    provider: Mapped[str | None] = mapped_column(String(255))
    redirect_uris: Mapped[str] = mapped_column(String(), nullable=False)
    grant_types: Mapped[str] = mapped_column(String(), nullable=False)
    revoked: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    personal_access_client: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    user_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True))
    redirect: Mapped[str | None] = mapped_column(String())

class OauthDeviceCodes(Base):
    __tablename__ = 'oauth_device_codes'
    __table_args__ = (UniqueConstraint('user_code', name='oauth_device_codes_user_code_unique'),)
    id: Mapped[str] = mapped_column(String(80), primary_key=True)
    user_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True))
    client_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    user_code: Mapped[str] = mapped_column(String(8), nullable=False)
    scopes: Mapped[str] = mapped_column(String(), nullable=False)
    revoked: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    user_approved_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    last_polled_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    expires_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class OauthRefreshTokens(Base):
    __tablename__ = 'oauth_refresh_tokens'
    id: Mapped[str] = mapped_column(String(80), primary_key=True)
    access_token_id: Mapped[str] = mapped_column(String(80), nullable=False)
    revoked: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    expires_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class OrgExePolicies(Base):
    __tablename__ = 'org_exe_policies'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    organization_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('organizations.id'), nullable=False)
    file_path: Mapped[str | None] = mapped_column(String(255))
    executed_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class OrgPolicies(Base):
    __tablename__ = 'org_policies'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    organization_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('organizations.id'))
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    policy_type: Mapped[str | None] = mapped_column(String(255))
    template: Mapped[str | None] = mapped_column(String())
    created_by: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id'))
    department: Mapped[str | None] = mapped_column(String(255))
    category: Mapped[str | None] = mapped_column(String(255))
    workforce_assignments: Mapped[Any | None] = mapped_column(JSON())
    status: Mapped[str] = mapped_column(String(255), nullable=False)
    effective_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    created_by_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)

class OrganizationCertificateClauses(Base):
    __tablename__ = 'organization_certificate_clauses'
    __table_args__ = (UniqueConstraint('organization_id', 'certificate_id', 'clause_id', name='org_cert_clause_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    organization_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('organizations.id'), nullable=False)
    certificate_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('certificates.id'))
    clause_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('clauses.id'))
    assigned_by: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True))
    status: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class OrganizationCertificateControls(Base):
    __tablename__ = 'organization_certificate_controls'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    organization_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('organizations.id'), nullable=False)
    certificate_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('certificates.id'), nullable=False)
    clause_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('clauses.id'), nullable=False)
    control_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('controls.id'), nullable=False)
    assigned_by: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id'))
    assignee_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id'))
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    status: Mapped[str | None] = mapped_column(String(255))
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class OrganizationCertificates(Base):
    __tablename__ = 'organization_certificates'
    __table_args__ = (UniqueConstraint('organization_id', 'certificate_id', name='org_cert_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    organization_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('organizations.id'), nullable=False)
    certificate_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('certificates.id'), nullable=False)
    labels: Mapped[Any | None] = mapped_column(JSON())
    assigned_by: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True))
    status: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class OrganizationInternalControls(Base):
    __tablename__ = 'organization_internal_controls'
    __table_args__ = (UniqueConstraint('organization_control_id', 'internal_control_id', name='organization_internal_controls_organization_control_id_internal'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    organization_control_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('organization_certificate_controls.id'), nullable=False)
    internal_control_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('internal_controls.id'), nullable=False)
    implemented: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    owner_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id'))
    notes: Mapped[str | None] = mapped_column(String())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class OrganizationPolicies(Base):
    __tablename__ = 'organization_policies'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    organization_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('organizations.id'), nullable=False)
    policy_template_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('policy_templates.id'), nullable=False)
    title: Mapped[str | None] = mapped_column(String(255))
    custom_policy_doc: Mapped[str | None] = mapped_column(String())
    custom_policy_version: Mapped[str | None] = mapped_column(String())
    custom_policy_template: Mapped[str | None] = mapped_column(String())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class OrganizationPolicyClauses(Base):
    __tablename__ = 'organization_policy_clauses'
    __table_args__ = (UniqueConstraint('organization_id', 'policy_template_id', 'clause_id', name='unique_organization_policy_clause'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    organization_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('organizations.id'), nullable=False)
    policy_template_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('policy_templates.id'), nullable=False)
    clause_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('clauses.id'), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class OrganizationPolicyControlMappings(Base):
    __tablename__ = 'organization_policy_control_mappings'
    __table_args__ = (UniqueConstraint('organization_id', 'policy_template_id', 'control_id', name='organization_policy_control_mappings_organization_id_policy_tem'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    organization_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('organizations.id'), nullable=False)
    policy_template_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('policy_templates.id'), nullable=False)
    control_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('controls.id'), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class OrganizationVendors(Base):
    __tablename__ = 'organization_vendors'
    __table_args__ = (UniqueConstraint('organization_id', 'business_name', name='organization_vendors_organization_id_business_name_unique'), UniqueConstraint('organization_id', 'email', name='organization_vendors_organization_id_email_unique'), UniqueConstraint('organization_id', 'vendor_id', name='organization_vendors_organization_id_vendor_id_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    organization_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('organizations.id'), nullable=False)
    vendor_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('vendors.id'), nullable=False)
    business_name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class Organizations(Base):
    __tablename__ = 'organizations'
    __table_args__ = (UniqueConstraint('domain_name', name='organizations_domain_name_unique'), UniqueConstraint('name', name='organizations_name_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    name: Mapped[str | None] = mapped_column(String(250))
    domain_name: Mapped[str | None] = mapped_column(String(250))
    short_name: Mapped[str | None] = mapped_column(String(250))
    dark_logo: Mapped[str | None] = mapped_column(String(250))
    light_logo: Mapped[str | None] = mapped_column(String(250))
    status: Mapped[str] = mapped_column(String(255), nullable=False)
    primary_sector: Mapped[str | None] = mapped_column(String(250))
    secondary_sector: Mapped[str | None] = mapped_column(String(250))
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    onboard: Mapped[int | None] = mapped_column(Integer())
    organization_size: Mapped[str | None] = mapped_column(String(250))
    cloud_hosting_model: Mapped[str | None] = mapped_column(String(250))
    primary_country: Mapped[str | None] = mapped_column(String(250))
    secondary_sectors: Mapped[Any | None] = mapped_column(JSONB())
    types_of_data_handled: Mapped[Any | None] = mapped_column(JSONB())
    security_context: Mapped[Any | None] = mapped_column(JSONB())

class PasswordResetTokens(Base):
    __tablename__ = 'password_reset_tokens'
    email: Mapped[str] = mapped_column(String(255), primary_key=True)
    token: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class Permissions(Base):
    __tablename__ = 'permissions'
    __table_args__ = (UniqueConstraint('name', name='permissions_name_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    parent_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('permissions.id'))
    display_identifier: Mapped[str | None] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(String())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    deleted_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class PersonalAccessTokens(Base):
    __tablename__ = 'personal_access_tokens'
    __table_args__ = (UniqueConstraint('token', name='personal_access_tokens_token_unique'),)
    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)
    tokenable_type: Mapped[str] = mapped_column(String(255), nullable=False)
    tokenable_id: Mapped[int] = mapped_column(Integer(), nullable=False)
    name: Mapped[str] = mapped_column(String(), nullable=False)
    token: Mapped[str] = mapped_column(String(64), nullable=False)
    abilities: Mapped[str | None] = mapped_column(String())
    last_used_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    expires_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class PolicyApprovers(Base):
    __tablename__ = 'policy_approvers'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    policy_version_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('policy_versions.id'))
    approver_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id'))
    condition: Mapped[str | None] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(255), nullable=False)
    reviewed_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    approved_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class PolicyAssignees(Base):
    __tablename__ = 'policy_assignees'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    policy_version_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('policy_versions.id'), nullable=False)
    assignee_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('employees.id'))
    status: Mapped[str] = mapped_column(String(255), nullable=False)
    acknowledged_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class PolicyClauses(Base):
    __tablename__ = 'policy_clauses'
    __table_args__ = (UniqueConstraint('policy_template_id', 'clause_id', name='policy_clauses_policy_template_id_clause_id_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    policy_template_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('policy_templates.id'), nullable=False)
    clause_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('clauses.id'), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class PolicyControlMappings(Base):
    __tablename__ = 'policy_control_mappings'
    __table_args__ = (UniqueConstraint('policy_template_id', 'control_id', name='policy_control_mappings_policy_template_id_control_id_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    policy_template_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('policy_templates.id'), nullable=False)
    control_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('controls.id'), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class PolicyTemplates(Base):
    __tablename__ = 'policy_templates'
    __table_args__ = (UniqueConstraint('short_name', name='policy_templates_short_name_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    short_name: Mapped[str] = mapped_column(String(255), nullable=False)
    title: Mapped[str | None] = mapped_column(String(255))
    code: Mapped[str | None] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(String())
    template: Mapped[str | None] = mapped_column(String())
    security_group: Mapped[str | None] = mapped_column(String(255))
    group: Mapped[str | None] = mapped_column(String(255))
    highlights: Mapped[Any | None] = mapped_column(JSON())
    version: Mapped[str | None] = mapped_column(String(255))
    status: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class PolicyVersions(Base):
    __tablename__ = 'policy_versions'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    org_policy_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('org_policies.id'), nullable=False)
    version: Mapped[str | None] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(255), nullable=False)
    is_current: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    approved_by: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id'))
    policy_duration: Mapped[str | None] = mapped_column(String(255))
    effective_at: Mapped[dt.date | None] = mapped_column(Date())
    next_review_at: Mapped[dt.date | None] = mapped_column(Date())
    expired_at: Mapped[dt.date | None] = mapped_column(Date())
    published_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    diff_data: Mapped[Any | None] = mapped_column(JSON())
    checkpoint_template: Mapped[str | None] = mapped_column(String())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class Reports(Base):
    __tablename__ = 'reports'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    organization_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('organizations.id'), nullable=False)
    report_title: Mapped[str] = mapped_column(String(255), nullable=False)
    report_type: Mapped[str] = mapped_column(String(255), nullable=False)
    export_format: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[str] = mapped_column(String(255), nullable=False)
    start_date: Mapped[dt.date | None] = mapped_column(Date())
    end_date: Mapped[dt.date | None] = mapped_column(Date())
    report_data: Mapped[Any | None] = mapped_column(JSON())
    file_path: Mapped[str | None] = mapped_column(String(255))
    generated_by: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True))
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class RiskControls(Base):
    __tablename__ = 'risk_controls'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    risk_library_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('risk_libraries.id'), nullable=False)
    control_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('controls.id'), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class RiskLibraries(Base):
    __tablename__ = 'risk_libraries'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(String())
    category: Mapped[str | None] = mapped_column(String(255))
    sub_category: Mapped[str | None] = mapped_column(String(255))
    sector: Mapped[Any | None] = mapped_column(JSONB())
    org_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('organizations.id'))
    suggest_likelihood: Mapped[int | None] = mapped_column(Integer())
    suggest_impact: Mapped[int | None] = mapped_column(Integer())
    threat_source: Mapped[str | None] = mapped_column(String(255))
    cia: Mapped[Any | None] = mapped_column(JSONB())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class RiskRegisters(Base):
    __tablename__ = 'risk_registers'
    __table_args__ = (UniqueConstraint('organization_id', 'risk_id', name='risk_register_org_risk_id_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    organization_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('organizations.id'), nullable=False)
    risk_library_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('risk_libraries.id'))
    owner_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id'))
    risk_id: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[str] = mapped_column(String(255), nullable=False)
    ai_status: Mapped[str] = mapped_column(String(255), nullable=False)
    llm_response: Mapped[Any | None] = mapped_column(JSON())
    risk_scores: Mapped[Any | None] = mapped_column(JSONB())
    identified_date: Mapped[dt.date | None] = mapped_column(Date())
    due_date: Mapped[dt.date | None] = mapped_column(Date())
    tags: Mapped[Any | None] = mapped_column(JSON())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class RolePermission(Base):
    __tablename__ = 'role_permission'
    __table_args__ = (UniqueConstraint('role_id', 'permission_id', name='role_permission_role_id_permission_id_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    role_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('roles.id'), nullable=False)
    permission_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('permissions.id'), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class Roles(Base):
    __tablename__ = 'roles'
    __table_args__ = (UniqueConstraint('name', name='roles_name_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    guard_name: Mapped[str | None] = mapped_column(String(100))
    description: Mapped[str | None] = mapped_column(String())
    status: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    deleted_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class Sessions(Base):
    __tablename__ = 'sessions'
    id: Mapped[str] = mapped_column(String(255), primary_key=True)
    user_id: Mapped[int | None] = mapped_column(Integer())
    ip_address: Mapped[str | None] = mapped_column(String(45))
    user_agent: Mapped[str | None] = mapped_column(String())
    payload: Mapped[str] = mapped_column(String(), nullable=False)
    last_activity: Mapped[int] = mapped_column(Integer(), nullable=False)

class SsoProviders(Base):
    __tablename__ = 'sso_providers'
    __table_args__ = (UniqueConstraint('name', name='sso_providers_name_unique'), UniqueConstraint('slug', name='sso_providers_slug_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(255), nullable=False)
    configuration_keys: Mapped[Any | None] = mapped_column(JSON())
    image_path: Mapped[str | None] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class SsoSetups(Base):
    __tablename__ = 'sso_setups'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    organization_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('organizations.id'))
    sso_provider_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('sso_providers.id'))
    configuration_data: Mapped[Any | None] = mapped_column(JSON())
    status: Mapped[str | None] = mapped_column(String(255))
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    validated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class States(Base):
    __tablename__ = 'states'
    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    country_id: Mapped[int] = mapped_column(Integer(), ForeignKey('countries.id'), nullable=False)
    country_code: Mapped[str | None] = mapped_column(String(255))
    fips_code: Mapped[str | None] = mapped_column(String(255))
    iso2: Mapped[str | None] = mapped_column(String(255))
    latitude: Mapped[str | None] = mapped_column(String(255))
    longitude: Mapped[str | None] = mapped_column(String(255))
    flag: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    wikiDataId: Mapped[str | None] = mapped_column(String())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class SubCategories(Base):
    __tablename__ = 'sub_categories'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    category_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('categories.id'))
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(String())
    status: Mapped[str | None] = mapped_column(String())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class SuggestEvidence(Base):
    __tablename__ = 'suggest_evidence'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class SuggestEvidenceControlMappings(Base):
    __tablename__ = 'suggest_evidence_control_mappings'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    suggest_evidence_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('suggest_evidence.id'), nullable=False)
    control_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('controls.id'), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class TaskAttachments(Base):
    __tablename__ = 'task_attachments'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    task_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('tasks.id'), nullable=False)
    name: Mapped[str | None] = mapped_column(String(255))
    source: Mapped[str | None] = mapped_column(String(255))
    file_type: Mapped[str | None] = mapped_column(String(255))
    updated_by: Mapped[str | None] = mapped_column(String(255))
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class Tasks(Base):
    __tablename__ = 'tasks'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    taskable_type: Mapped[str] = mapped_column(String(255), nullable=False)
    taskable_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    name: Mapped[str | None] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(String())
    priority: Mapped[str | None] = mapped_column(String(255))
    owner_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id'))
    status: Mapped[str] = mapped_column(String(255), nullable=False)
    estimated_effort: Mapped[str | None] = mapped_column(String(255))
    due_date: Mapped[dt.date | None] = mapped_column(Date())
    category: Mapped[str | None] = mapped_column(String(255))
    subcategory: Mapped[str | None] = mapped_column(String(255))
    evidence_collection_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('evidence_collections.id'))
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class TempPolicyUploads(Base):
    __tablename__ = 'temp_policy_uploads'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    organization_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('organizations.id'), nullable=False)
    policy_name: Mapped[str] = mapped_column(String(255), nullable=False)
    policy_version: Mapped[str] = mapped_column(String(255), nullable=False)
    file_path: Mapped[str] = mapped_column(String(255), nullable=False)
    file_url: Mapped[str] = mapped_column(String(255), nullable=False)
    original_filename: Mapped[str] = mapped_column(String(255), nullable=False)
    file_hash: Mapped[str | None] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(255), nullable=False)
    created_by: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id'))
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class TempTasks(Base):
    __tablename__ = 'temp_tasks'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    taskable_type: Mapped[str] = mapped_column(String(255), nullable=False)
    taskable_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    name: Mapped[str | None] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(String())
    priority: Mapped[str | None] = mapped_column(String(255))
    owner_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id'))
    status: Mapped[str] = mapped_column(String(255), nullable=False)
    estimated_effort: Mapped[str | None] = mapped_column(String(255))
    due_date: Mapped[dt.date | None] = mapped_column(Date())
    category: Mapped[str | None] = mapped_column(String(255))
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class TempVendors(Base):
    __tablename__ = 'temp_vendors'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    business_name: Mapped[str | None] = mapped_column(String(255))
    poc_name: Mapped[str | None] = mapped_column(String(255))
    email: Mapped[str | None] = mapped_column(String(255))
    phone: Mapped[str | None] = mapped_column(String(255))
    address: Mapped[str | None] = mapped_column(String(255))
    country: Mapped[str | None] = mapped_column(String(255))
    data_exposure: Mapped[str | None] = mapped_column(String(255))
    category_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('categories.id'))
    sub_category_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('sub_categories.id'))
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class ToolIntegrations(Base):
    __tablename__ = 'tool_integrations'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    user_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    organization_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('organizations.id'), nullable=False)
    tool_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('tools.id'), nullable=False)
    configuration_data: Mapped[Any | None] = mapped_column(JSON())
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class Tools(Base):
    __tablename__ = 'tools'
    __table_args__ = (UniqueConstraint('name', name='tools_name_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    name: Mapped[str | None] = mapped_column(String(255))
    image_path: Mapped[str | None] = mapped_column(String(255))
    configuration_keys: Mapped[Any | None] = mapped_column(JSON())
    status: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str | None] = mapped_column(String(255))
    sync_type: Mapped[str | None] = mapped_column(String())
    scope: Mapped[Any | None] = mapped_column(JSON())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class TrustCenterConfigs(Base):
    __tablename__ = 'trust_center_configs'
    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)
    status: Mapped[int] = mapped_column(Integer(), nullable=False)
    description: Mapped[str | None] = mapped_column(String(255))
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class TrustCenters(Base):
    __tablename__ = 'trust_centers'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    provider: Mapped[str] = mapped_column(String(255), nullable=False)
    url: Mapped[str | None] = mapped_column(String(255))
    privacy_url: Mapped[str | None] = mapped_column(String(255))
    terms_url: Mapped[str | None] = mapped_column(String(255))
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class TrustcenterAccessRequests(Base):
    __tablename__ = 'trustcenter_access_requests'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    company_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('trustcenter_companies.id'), nullable=False)
    first_name: Mapped[str] = mapped_column(String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(String(255), nullable=False)
    requester_email: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[str] = mapped_column(String(255), nullable=False)
    message: Mapped[str | None] = mapped_column(String())
    denial_reason: Mapped[str | None] = mapped_column(String())
    access_token: Mapped[str | None] = mapped_column(String(255))
    token_expires: Mapped[dt.datetime | None] = mapped_column(DateTime())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class TrustcenterAccessRules(Base):
    __tablename__ = 'trustcenter_access_rules'
    __table_args__ = (UniqueConstraint('user_id', name='trustcenter_access_rules_user_id_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    user_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('trustcenter_users.id'), nullable=False)
    require_email: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    domain_whitelist: Mapped[str | None] = mapped_column(String())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class TrustcenterActivityLogs(Base):
    __tablename__ = 'trustcenter_activity_logs'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    user_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('trustcenter_users.id'))
    action: Mapped[str] = mapped_column(String(), nullable=False)
    entity_type: Mapped[str | None] = mapped_column(String(100))
    entity_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True))
    ip_address: Mapped[str | None] = mapped_column(String(50))
    metadata: Mapped[Any | None] = mapped_column(JSON())
    created_at: Mapped[dt.datetime] = mapped_column(DateTime(), nullable=False)

class TrustcenterBranding(Base):
    __tablename__ = 'trustcenter_branding'
    user_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('trustcenter_users.id'), primary_key=True)
    logo_url: Mapped[str | None] = mapped_column(String())
    page_title: Mapped[str | None] = mapped_column(String())
    tagline: Mapped[str | None] = mapped_column(String(500))
    primary_color: Mapped[str | None] = mapped_column(String(50))
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class TrustcenterCertifications(Base):
    __tablename__ = 'trustcenter_certifications'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    company_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('trustcenter_companies.id'), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(String())
    status: Mapped[str] = mapped_column(String(255), nullable=False)
    badge_url: Mapped[str | None] = mapped_column(String(500))
    display_order: Mapped[int] = mapped_column(Integer(), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class TrustcenterCompanies(Base):
    __tablename__ = 'trustcenter_companies'
    __table_args__ = (UniqueConstraint('name', name='trustcenter_companies_name_unique'), UniqueConstraint('slug', name='trustcenter_companies_slug_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(String())
    plan: Mapped[str] = mapped_column(String(64), nullable=False)
    support_email: Mapped[str | None] = mapped_column(String(255))
    aws_access_key_id: Mapped[str | None] = mapped_column(String(255))
    aws_secret_access_key: Mapped[str | None] = mapped_column(String())
    aws_region: Mapped[str | None] = mapped_column(String(64))
    azure_client_id: Mapped[str | None] = mapped_column(String(255))
    azure_client_secret: Mapped[str | None] = mapped_column(String())
    azure_tenant_id: Mapped[str | None] = mapped_column(String(255))
    azure_subscription_id: Mapped[str | None] = mapped_column(String(255))
    gcp_project_id: Mapped[str | None] = mapped_column(String(255))
    gcp_service_account_key: Mapped[str | None] = mapped_column(String())
    custom_domain: Mapped[str | None] = mapped_column(String(255))
    domain_type: Mapped[str | None] = mapped_column(String(255))
    domain_ip_address: Mapped[str | None] = mapped_column(String(45))
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    organization_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True))

class TrustcenterCompanyControls(Base):
    __tablename__ = 'trustcenter_company_controls'
    __table_args__ = (UniqueConstraint('company_id', 'control_id', name='trustcenter_company_controls_company_id_control_id_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    company_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('trustcenter_companies.id'), nullable=False)
    control_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('controls.id'), nullable=False)
    is_active: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class TrustcenterContactRequests(Base):
    __tablename__ = 'trustcenter_contact_requests'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    company: Mapped[str | None] = mapped_column(String(255))
    subject: Mapped[str] = mapped_column(String(255), nullable=False)
    message: Mapped[str] = mapped_column(String(), nullable=False)
    status: Mapped[str] = mapped_column(String(255), nullable=False)
    ip_address: Mapped[str | None] = mapped_column(String(50))
    user_agent: Mapped[str | None] = mapped_column(String())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class TrustcenterControls(Base):
    __tablename__ = 'trustcenter_controls'
    __table_args__ = (UniqueConstraint('short_name', name='trustcenter_controls_short_name_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
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

class TrustcenterDocuments(Base):
    __tablename__ = 'trustcenter_documents'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    user_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('trustcenter_users.id'), nullable=False)
    file_name: Mapped[str] = mapped_column(String(255), nullable=False)
    file_path: Mapped[str] = mapped_column(String(500), nullable=False)
    file_size: Mapped[int | None] = mapped_column(Integer())
    mime_type: Mapped[str | None] = mapped_column(String(100))
    title: Mapped[str | None] = mapped_column(String(255))
    expiry_date: Mapped[dt.datetime | None] = mapped_column(DateTime())
    is_locked: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    is_public: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class TrustcenterFaqs(Base):
    __tablename__ = 'trustcenter_faqs'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    company_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('trustcenter_companies.id'), nullable=False)
    question: Mapped[str] = mapped_column(String(), nullable=False)
    answer: Mapped[str] = mapped_column(String(), nullable=False)
    display_order: Mapped[int] = mapped_column(Integer(), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class TrustcenterLeadership(Base):
    __tablename__ = 'trustcenter_leadership'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    company_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('trustcenter_companies.id'), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    bio: Mapped[str | None] = mapped_column(String())
    image_url: Mapped[str | None] = mapped_column(String(500))
    linkedin_url: Mapped[str | None] = mapped_column(String(500))
    display_order: Mapped[int] = mapped_column(Integer(), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class TrustcenterPlans(Base):
    __tablename__ = 'trustcenter_plans'
    __table_args__ = (UniqueConstraint('key', name='trustcenter_plans_key_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    key: Mapped[str] = mapped_column(String(64), nullable=False)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    price: Mapped[str | None] = mapped_column(String(64))
    description: Mapped[str | None] = mapped_column(String())
    features: Mapped[Any] = mapped_column(JSONB(), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class TrustcenterSubprocessors(Base):
    __tablename__ = 'trustcenter_subprocessors'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    company_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('trustcenter_companies.id'), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(String())
    logo_url: Mapped[str | None] = mapped_column(String(500))
    website: Mapped[str | None] = mapped_column(String(500))
    display_order: Mapped[int] = mapped_column(Integer(), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class TrustcenterUsers(Base):
    __tablename__ = 'trustcenter_users'
    __table_args__ = (UniqueConstraint('email', name='trustcenter_users_email_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    company: Mapped[str | None] = mapped_column(String(255))
    company_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('trustcenter_companies.id'))
    role: Mapped[str | None] = mapped_column(String(255))
    is_email_verified: Mapped[bool | None] = mapped_column(Boolean())
    is_active: Mapped[bool | None] = mapped_column(Boolean())
    verification_code_hash: Mapped[str | None] = mapped_column(String(255))
    verification_expires_at: Mapped[dt.datetime | None] = mapped_column(DateTime(timezone=True))
    deleted_at: Mapped[dt.datetime | None] = mapped_column(DateTime(timezone=True))
    is_published: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    reset_token: Mapped[str | None] = mapped_column(String(255))
    reset_token_expires_at: Mapped[dt.datetime | None] = mapped_column(DateTime(timezone=True))
    welcome_popup_seen: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime(timezone=True))
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime(timezone=True))
    organization_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True))
    product: Mapped[str | None] = mapped_column(String(255))

class UserRoleOrganizations(Base):
    __tablename__ = 'user_role_organizations'
    __table_args__ = (UniqueConstraint('assignable_type', 'assignable_id', 'role_id', 'organization_id', name='uro_assignable_role_org_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    assignable_type: Mapped[str | None] = mapped_column(String(255))
    assignable_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True))
    role_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('roles.id'), nullable=False)
    organization_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('organizations.id'), nullable=False)
    status: Mapped[str] = mapped_column(String(255), nullable=False)
    is_primary: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class UserWebTokens(Base):
    __tablename__ = 'user_web_tokens'
    __table_args__ = (UniqueConstraint('token', name='user_web_tokens_token_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    tokenable_type: Mapped[str | None] = mapped_column(String(255))
    tokenable_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True))
    organization_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('organizations.id'))
    token: Mapped[str] = mapped_column(String(255), nullable=False)
    purpose: Mapped[str | None] = mapped_column(String(255))
    expires_at: Mapped[dt.datetime] = mapped_column(DateTime(), nullable=False)
    is_used: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    status: Mapped[str | None] = mapped_column(String(255))
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class Users(Base):
    __tablename__ = 'users'
    __table_args__ = (UniqueConstraint('email', name='users_email_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    name: Mapped[str | None] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    password: Mapped[str | None] = mapped_column(String(255))
    google2fa_secret: Mapped[str | None] = mapped_column(String())
    two_factor_verified: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    is_completed: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    email_verified_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    provider: Mapped[str | None] = mapped_column(String(255))
    provider_id: Mapped[str | None] = mapped_column(String(255))
    last_login_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    last_initial_page: Mapped[str | None] = mapped_column(String(255))
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    product: Mapped[str | None] = mapped_column(String(255))
    company_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True))
    company: Mapped[str | None] = mapped_column(String(255))
    role: Mapped[str | None] = mapped_column(String(255))
    active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    verification_code_hash: Mapped[str | None] = mapped_column(String(255))
    verification_expires: Mapped[dt.datetime | None] = mapped_column(DateTime())
    published: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    welcome_popup_seen: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    reset_token: Mapped[str | None] = mapped_column(String(255))
    reset_token_expires: Mapped[dt.datetime | None] = mapped_column(DateTime())
    email_verified: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    deleted_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class VendorAssessmentQuestionBankTemps(Base):
    __tablename__ = 'vendor_assessment_question_bank_temps'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    organization_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True))
    certificate_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True))
    vendor_type: Mapped[str | None] = mapped_column(String(255))
    department: Mapped[str | None] = mapped_column(String(255))
    question: Mapped[str | None] = mapped_column(String())
    type: Mapped[str | None] = mapped_column(String(255))
    data_exposure: Mapped[str | None] = mapped_column(String(255))
    weightage: Mapped[Any | None] = mapped_column(JSON())
    is_attachment: Mapped[Any | None] = mapped_column(JSON())
    description: Mapped[str | None] = mapped_column(String())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class VendorAssessmentQuestionBanks(Base):
    __tablename__ = 'vendor_assessment_question_banks'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    organization_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('organizations.id'))
    certificate_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('certificates.id'))
    vendor_type: Mapped[str | None] = mapped_column(String(255))
    department: Mapped[str | None] = mapped_column(String(255))
    question: Mapped[str | None] = mapped_column(String())
    type: Mapped[str | None] = mapped_column(String(255))
    data_exposure: Mapped[str | None] = mapped_column(String(255))
    weightage: Mapped[Any | None] = mapped_column(JSON())
    is_attachment: Mapped[Any | None] = mapped_column(JSON())
    description: Mapped[str | None] = mapped_column(String())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class VendorAssessmentQuestions(Base):
    __tablename__ = 'vendor_assessment_questions'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    vendor_assessment_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('vendor_assessments.id'), nullable=False)
    vendor_assessment_question_bank_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('vendor_assessment_question_banks.id'), nullable=False)
    answer: Mapped[Any | None] = mapped_column(JSON())
    answer_text: Mapped[str | None] = mapped_column(String())
    score: Mapped[Any | None] = mapped_column(JSON())
    status: Mapped[str | None] = mapped_column(String(255))
    reference: Mapped[str | None] = mapped_column(String())
    description: Mapped[str | None] = mapped_column(String())
    llm_response: Mapped[Any | None] = mapped_column(JSON())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class VendorAssessments(Base):
    __tablename__ = 'vendor_assessments'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    vendor_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('vendors.id'), nullable=False)
    data_exposure: Mapped[str] = mapped_column(String(), nullable=False)
    severity: Mapped[str | None] = mapped_column(String(255))
    result: Mapped[Any | None] = mapped_column(JSON())
    contracts_expiry_date: Mapped[dt.date | None] = mapped_column(Date())
    last_assessment_date: Mapped[dt.date | None] = mapped_column(Date())
    next_assessment_date: Mapped[dt.date | None] = mapped_column(Date())
    completed_on: Mapped[dt.date | None] = mapped_column(Date())
    page: Mapped[str | None] = mapped_column(String(255))
    status: Mapped[str | None] = mapped_column(String(255))
    llm_request: Mapped[Any | None] = mapped_column(JSON())
    llm_response: Mapped[Any | None] = mapped_column(JSON())
    llm_status: Mapped[str | None] = mapped_column(String(255))
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class VendorCertificateDetails(Base):
    __tablename__ = 'vendor_certificate_details'
    __table_args__ = (UniqueConstraint('vendor_id', 'vendor_assessment_id', name='vendor_cert_unique'),)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    vendor_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('vendors.id'), nullable=False)
    vendor_assessment_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('vendor_assessments.id'), nullable=False)
    framework: Mapped[str | None] = mapped_column(String(255))
    certification_date: Mapped[dt.date | None] = mapped_column(Date())
    issued_by: Mapped[str | None] = mapped_column(String(255))
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class VendorCertificateDocuments(Base):
    __tablename__ = 'vendor_certificate_documents'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    vendor_certificate_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    path: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class VendorDetails(Base):
    __tablename__ = 'vendor_details'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    vendor_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('vendors.id'), nullable=False)
    email: Mapped[str | None] = mapped_column(String(255))
    password: Mapped[str | None] = mapped_column(String(255))
    contact_phone: Mapped[str | None] = mapped_column(String(255))
    country: Mapped[str | None] = mapped_column(String(255))
    country_code: Mapped[str | None] = mapped_column(String(255))
    country_by: Mapped[str | None] = mapped_column(String(255))
    state: Mapped[str | None] = mapped_column(String(255))
    address: Mapped[str | None] = mapped_column(String())
    profile_img: Mapped[str | None] = mapped_column(String(255))
    mode: Mapped[str | None] = mapped_column(String(255))
    status: Mapped[str | None] = mapped_column(String(255))
    contract_start_date: Mapped[dt.date | None] = mapped_column(Date())
    contract_end_date: Mapped[dt.date | None] = mapped_column(Date())
    contract_frequency: Mapped[str | None] = mapped_column(String(255))
    provider: Mapped[str | None] = mapped_column(String(255))
    provider_id: Mapped[str | None] = mapped_column(String(255))
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class VendorEvidence(Base):
    __tablename__ = 'vendor_evidence'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    vendor_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('vendors.id'), nullable=False)
    vendor_assessment_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('vendor_assessments.id'), nullable=False)
    vendor_assessment_question_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('vendor_assessment_questions.id'), nullable=False)
    name: Mapped[str | None] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(String(255))
    path: Mapped[str | None] = mapped_column(String(255))
    url: Mapped[str | None] = mapped_column(String(255))
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class VendorLlmProcesses(Base):
    __tablename__ = 'vendor_llm_processes'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    vendor_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('vendors.id'), nullable=False)
    vendor_assessment_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('vendor_assessments.id'), nullable=False)
    organization_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('organizations.id'), nullable=False)
    selected_pages: Mapped[Any | None] = mapped_column(JSON())
    llm_request: Mapped[Any | None] = mapped_column(JSON())
    llm_response: Mapped[Any | None] = mapped_column(JSON())
    llm_status: Mapped[str] = mapped_column(String(255), nullable=False)
    error_message: Mapped[str | None] = mapped_column(String())
    retry_count: Mapped[int] = mapped_column(Integer(), nullable=False)
    processed_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class VendorPageData(Base):
    __tablename__ = 'vendor_page_data'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    vendor_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('vendors.id'), nullable=False)
    vendor_assessment_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('vendor_assessments.id'), nullable=False)
    page_type: Mapped[str] = mapped_column(String(255), nullable=False)
    data: Mapped[Any | None] = mapped_column(JSON())
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class VendorPageDocuments(Base):
    __tablename__ = 'vendor_page_documents'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    vendor_page_data_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('vendor_page_data.id'), nullable=False)
    path: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class VendorTrustCenters(Base):
    __tablename__ = 'vendor_trust_centers'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    vendor_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('vendors.id'))
    vendor_assessment_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('vendor_assessments.id'))
    provider: Mapped[str | None] = mapped_column(String(255))
    url: Mapped[str | None] = mapped_column(String(255))
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class Vendors(Base):
    __tablename__ = 'vendors'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    business_name: Mapped[str] = mapped_column(String(255), nullable=False)
    poc_name: Mapped[str | None] = mapped_column(String(255))
    website_url: Mapped[str | None] = mapped_column(String(255))
    vendor_type: Mapped[str | None] = mapped_column(String(255))
    is_confirmed: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    category_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('categories.id'))
    sub_category_id: Mapped[UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('sub_categories.id'))
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

class Vulnerabilities(Base):
    __tablename__ = 'vulnerabilities'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    organization_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('organizations.id'), nullable=False)
    platform: Mapped[str | None] = mapped_column(String(255))
    scope: Mapped[str | None] = mapped_column(String(255))
    vulnerability_id: Mapped[str | None] = mapped_column(String(255))
    vulnerability_name: Mapped[str | None] = mapped_column(String(255))
    discovered_at: Mapped[dt.date | None] = mapped_column(Date())
    risk_score: Mapped[str | None] = mapped_column(String(255))
    severity: Mapped[str | None] = mapped_column(String(255))
    action_at: Mapped[dt.date | None] = mapped_column(Date())
    type: Mapped[str | None] = mapped_column(String(255))
    tags: Mapped[str | None] = mapped_column(String(255))
    agent_check_in: Mapped[str | None] = mapped_column(String(255))
    status: Mapped[str | None] = mapped_column(String(255))
    created_at: Mapped[dt.datetime | None] = mapped_column(DateTime())
    updated_at: Mapped[dt.datetime | None] = mapped_column(DateTime())

