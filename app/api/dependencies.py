"""API dependencies."""
from typing import Annotated
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_session
from app.services.story import StoryService


SessionDep = Annotated[AsyncSession, Depends(get_session)]


def get_story_service(session: SessionDep):
    """Get a story service."""
    return StoryService(session)


ServiceDep = Annotated[StoryService, Depends(get_story_service)]
