# ruff: noqa: A002, FAST002
from fastapi import APIRouter, Query

from src.dependencies.services import IncidentServiceDep
from src.domain.entities.incident import CreateIncidentRequestEntity, IncidentEntity, UpdateIncidentRequestEntity

router = APIRouter()


@router.get("/incident")
async def list_incident(service: IncidentServiceDep, status: str | None = Query(None)) -> list[IncidentEntity]:
    return await service.list_incidents(status=status)


@router.post("/incident")
async def create_incident(service: IncidentServiceDep, request: CreateIncidentRequestEntity) -> IncidentEntity:
    return await service.create_incident(request=request)


@router.patch("/incident/{id}")
async def update_incident_status(id: int, service: IncidentServiceDep, request: UpdateIncidentRequestEntity) -> IncidentEntity:
    return await service.update_incident(id=id, request=request)
