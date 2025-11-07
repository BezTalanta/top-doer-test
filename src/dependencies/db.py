from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.settings import sqlite_settings

ENGINE = create_async_engine(sqlite_settings.sqlalchemy_async_sqlite_url)

SESSIONMAKER = async_sessionmaker(bind=ENGINE, expire_on_commit=False)


async def session_factory() -> AsyncSession:
    async with SESSIONMAKER() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(session_factory)]
