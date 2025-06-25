from typing import Any

from my_namespace.my_component import DataModel
from sqlalchemy import TIMESTAMP, BigInteger, Integer, PrimaryKeyConstraint, String
from sqlalchemy.orm import Mapped, mapped_column

from .core import BronzeBriDB

class Companies(BronzeBriDB, DataModel):
    """Table class from the Bri Bronze Companies.

    Args:
        BriBronzeDB (class): The Bronze BRI specific base class.
        DataModel (class): The base data model.

    """

    __tablename__ = "companies"
    __table_args__ = (PrimaryKeyConstraint("id", name="companies_pk"),)

    record_uuid: Mapped[str | None] = mapped_column(String)
    Op: Mapped[str | None] = mapped_column(String)
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str | None] = mapped_column(String)
    state: Mapped[str | None] = mapped_column(String)
    account_type: Mapped[str | None] = mapped_column(String)
    seats_number: Mapped[int | None] = mapped_column(Integer)
    requests_number: Mapped[int | None] = mapped_column(Integer)
    subscription_expire_at: Mapped[Any | None] = mapped_column(TIMESTAMP)
    created_at: Mapped[Any | None] = mapped_column(TIMESTAMP)
    updated_at: Mapped[Any | None] = mapped_column(TIMESTAMP)
    subscription_starts_at: Mapped[Any | None] = mapped_column(TIMESTAMP)
    registration_form_header: Mapped[str | None] = mapped_column(String)
    registration_form_video_code: Mapped[str | None] = mapped_column(String)
    registration_form_wysiwyg: Mapped[str | None] = mapped_column(String)
    profile_views_number: Mapped[int | None] = mapped_column(Integer)
    salesforce_token: Mapped[str | None] = mapped_column(String)
    salesforce_auto_registration: Mapped[str | None] = mapped_column(String)
    deleted_at: Mapped[Any | None] = mapped_column(TIMESTAMP)
    profile_downloads_number: Mapped[int | None] = mapped_column(Integer)
    legacy_id: Mapped[int | None] = mapped_column(BigInteger)
    projects_number: Mapped[int | None] = mapped_column(Integer)
    show_previous_interval_data: Mapped[str | None] = mapped_column(String)
    project_sharing_available: Mapped[str | None] = mapped_column(String)
    project_sharing_to_new_company_members_available: Mapped[str | None] = (
        mapped_column(String)
    )
    manager_id: Mapped[int | None] = mapped_column(BigInteger)
    slug: Mapped[str | None] = mapped_column(String)
    batch_id: Mapped[int | None] = mapped_column(BigInteger)
    record_created_timestamp: Mapped[Any | None] = mapped_column(TIMESTAMP)
    record_updated_timestamp: Mapped[Any | None] = mapped_column(TIMESTAMP)
    record_job_log_key: Mapped[str | None] = mapped_column(String)
    commit_timestamp: Mapped[Any | None] = mapped_column(TIMESTAMP)

