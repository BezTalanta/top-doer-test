from typing import Annotated

from fastapi import Depends

from src.dependencies.db import SessionDep
from src.domain.repositories.incident_repository_base import BaseIncidentRepository
from src.infrastructure.repositories.incident_repository import IncidentRepository


async def incident_repository_factory(session: SessionDep) -> BaseIncidentRepository:
    return IncidentRepository(session=session)


IncidentRepositoryDep = Annotated[BaseIncidentRepository, Depends(incident_repository_factory)]
