from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.models import Base


class IncidentSQLModel(Base):
    __tablename__ = "incidents"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    description: Mapped[str]
    status: Mapped[str]
    source: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
