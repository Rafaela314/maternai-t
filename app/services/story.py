"""Story service."""
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.story import Story as StorySchema
from app.api.schemas.story import StoryCreate, StoryUpdate
from app.database.models import Story as StoryModel


class StoryService:
    """Business logic for story persistence."""

    def __init__(self, session: AsyncSession):
        self.session = session

    @staticmethod
    def _to_schema(story: StoryModel) -> StorySchema:
        """Convert DB model to API schema."""
        return StorySchema.model_validate(story, from_attributes=True)

    async def get_story(self, story_id: int) -> StorySchema | None:
        """Get a story by id."""
        story = await self.session.get(StoryModel, story_id)
        if story is None:
            return None
        return self._to_schema(story)

    async def create_story(self, story_create: StoryCreate) -> StorySchema:
        """Create a new story."""
        data = story_create.model_dump()
        now = datetime.now()
        created_at = data.pop("created_at", now)

        new_story = StoryModel(
            **data,
            created_at=created_at,
            updated_at=now,
        )
        self.session.add(new_story)
        await self.session.commit()
        await self.session.refresh(new_story)

        return self._to_schema(new_story)

    async def update_story(
        self, story_id: int, story_update: StoryUpdate
    ) -> StorySchema | None:
        """Update a story."""
        story = await self.session.get(StoryModel, story_id)
        if story is None:
            return None

        update_data = story_update.model_dump(
            exclude_unset=True, exclude_none=True
        )
        if not update_data:
            return self._to_schema(story)

        update_data["updated_at"] = datetime.now()
        story.sqlmodel_update(update_data)

        self.session.add(story)
        await self.session.commit()
        await self.session.refresh(story)
        return self._to_schema(story)

    async def delete_story(self, story_id: int) -> bool:
        """Delete a story."""
        story = await self.session.get(StoryModel, story_id)
        if story is None:
            return False
        await self.session.delete(story)
        await self.session.commit()
        return True
