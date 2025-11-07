# ruff: noqa: A002
from src.domain.entities.incident import CreateIncidentRequestEntity, IncidentEntity, UpdateIncidentRequestEntity
from src.domain.repositories.incident_repository_base import BaseIncidentRepository


class IncidentService:
    def __init__(self, incident_repository: BaseIncidentRepository) -> None:
        self.incident_repository = incident_repository

    async def create_incident(self, request: CreateIncidentRequestEntity) -> IncidentEntity:
        return await self.incident_repository.create_incident(
            text=request.text,
            description=request.description,
            status=request.status,
            source=request.source,
        )

    async def update_incident(self, id: int, request: UpdateIncidentRequestEntity) -> IncidentEntity:
        return await self.incident_repository.update_incident(id=id, values={"status": request.status})

    async def list_incidents(self, status: str | None = None) -> list[IncidentEntity]:
        return await self.incident_repository.list_incidents(status=status)
