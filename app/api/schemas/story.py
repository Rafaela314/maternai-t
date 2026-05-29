"""Pydantic schemas for the Story API."""

from datetime import datetime
from pydantic import BaseModel, Field
from app.database.models import ModeOfDelivery, HealthCareType, PlaceOfDeliveryType


class BaseStory(BaseModel):
    """Base story model."""
    city: str
    country: str
    doctor: str
    doula: str | None = Field(default=None)
    health_care_type: HealthCareType
    midwife: str | None = Field(default=None)
    mode_of_delivery: ModeOfDelivery
    place_of_delivery_type: PlaceOfDeliveryType
    place_of_delivery: str = Field(max_length=100)
    rating: int = Field(ge=1, le=5)
    state: str
    summary: str
    title: str


class Story(BaseStory):
    """Story read model."""
    id: int
    created_at: datetime
    updated_at: datetime


class StoryCreate(BaseStory):
    """Story create model."""
    created_at: datetime = Field(default_factory=datetime.now)


class StoryUpdate(BaseModel):
    """Story update model."""
    city: str | None = Field(default=None)
    country: str | None = Field(default=None)
    doctor: str | None = Field(default=None)
    doula: str | None = Field(default=None)
    health_care_type: HealthCareType | None = Field(default=None)
    midwife: str | None = Field(default=None)
    mode_of_delivery: ModeOfDelivery | None = Field(default=None)
    place_of_delivery_type: PlaceOfDeliveryType | None = Field(default=None)
    place_of_delivery: str | None = Field(max_length=100, default=None)
    rating: int | None = Field(ge=1, le=5, default=None)
    state: str | None = Field(default=None)
    summary: str | None = Field(default=None)
    title: str | None = Field(default=None)
