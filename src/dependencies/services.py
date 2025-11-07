from typing import Annotated

from fastapi import Depends

from src.dependencies.repositories import IncidentRepositoryDep
from src.domain.incident_base import BaseIncidentService
from src.domain.services.incident import IncidentService


async def incident_service_factory(incident_repository: IncidentRepositoryDep) -> BaseIncidentService:
    return IncidentService(incident_repository=incident_repository)


IncidentServiceDep = Annotated[BaseIncidentService, Depends(incident_service_factory)]
