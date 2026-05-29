"""Story API routes."""
from fastapi import APIRouter
from fastapi import HTTPException, status
from app.api.schemas.story import Story, StoryCreate, StoryUpdate
from app.api.dependencies import ServiceDep


router = APIRouter()


@router.get("/story/{story_id}", response_model=Story)
async def get_story(story_id: int, service: ServiceDep):
    """Return a story by id."""
    story = await service.get_story(story_id)

    if story is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given id does not exist!",
        )
    return story


@router.post("/story")
async def submit_story(
    story: StoryCreate, service: ServiceDep
) -> Story:
    """Create a new story."""
    return await service.create_story(story)


@router.patch("/story/{story_id}", response_model=Story)
async def update_story(
    story_id: int,
    story_update: StoryUpdate,
    service: ServiceDep,
) -> Story:
    """Update an existing story."""
    update_data = story_update.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No fields to update",
        )

    story = await service.update_story(story_id, story_update)
    if story is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given id does not exist!",
        )

    return story


@router.delete("/story/{story_id}", status_code=status.HTTP_200_OK)
async def delete_story(
    story_id: int, service: ServiceDep
) -> dict[str, str]:
    """Delete a story by id."""
    deleted = await service.delete_story(story_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given id does not exist!",
        )
    return {"detail": "Story deleted successfully"}
