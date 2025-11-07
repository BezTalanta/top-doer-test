# ruff: noqa: A002
from typing import Protocol

from src.domain.entities.incident import CreateIncidentRequestEntity, IncidentEntity, UpdateIncidentRequestEntity


class BaseIncidentService(Protocol):
    async def create_incident(self, request: CreateIncidentRequestEntity) -> IncidentEntity:
        ...

    async def update_incident(self, id: int, request: UpdateIncidentRequestEntity) -> IncidentEntity:
        ...

    async def list_incidents(self, status: str | None = None) -> list[IncidentEntity]:
        ...
