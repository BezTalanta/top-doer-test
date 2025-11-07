# ruff: noqa: A002
from typing import Protocol

from src.domain.entities.incident import IncidentEntity


class BaseIncidentRepository(Protocol):
    async def create_incident(self, text: str, description: str, status: str, source: str) -> IncidentEntity: ...

    async def update_incident(self, id: int, values: dict) -> IncidentEntity: ...

    async def list_incidents(self, status: str | None = None) -> list[IncidentEntity]: ...
