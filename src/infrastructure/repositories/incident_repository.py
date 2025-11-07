# ruff: noqa: A002
from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.entities.incident import IncidentEntity
from src.infrastructure.models.incident import IncidentSQLModel


class IncidentRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    @staticmethod
    async def __map_incident_model_to_entity(model: IncidentSQLModel) -> IncidentEntity:
        return IncidentEntity(
            id=model.id,
            text=model.text,
            description=model.description,
            status=model.status,
            source=model.source,
            created_at=model.created_at,
        )

    async def create_incident(self, text: str, description: str, status: str, source: str) -> IncidentEntity:
        query = (
            insert(IncidentSQLModel).values(text=text, description=description, status=status, source=source).returning(IncidentSQLModel)
        )
        incident = (await self.session.execute(query)).scalar_one()
        await self.session.commit()
        return await self.__map_incident_model_to_entity(model=incident)

    async def update_incident(self, id: int, values: dict) -> IncidentEntity:
        query = update(IncidentSQLModel).where(IncidentSQLModel.id == id).values(**values).returning(IncidentSQLModel)
        incident = (await self.session.execute(query)).scalar_one()
        await self.session.commit()
        return await self.__map_incident_model_to_entity(model=incident)

    async def list_incidents(self, status: str | None = None) -> list[IncidentEntity]:
        query = select(IncidentSQLModel)
        if status is not None:
            query = query.where(IncidentSQLModel.status.ilike(f"%{status}%"))
        incidents = (await self.session.execute(query)).scalars().all()
        return [await self.__map_incident_model_to_entity(incident) for incident in incidents]
