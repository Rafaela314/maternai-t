"""Database session."""
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

from app.database.config import settings


engine = create_async_engine(
    url=settings.DB_SOURCE,
    echo=True)


async def create_db_tables():
    """Create the database tables."""
    async with engine.begin() as connection:
        from .models import Story  # noqa: F401 — registers table with metadata
        await connection.run_sync(SQLModel.metadata.create_all)


async def get_session():
    """Get a session from the database."""
    async_session = sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    async with async_session() as session:
        yield session
