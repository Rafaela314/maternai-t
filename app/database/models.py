"""Database models."""
from enum import Enum
from sqlmodel import Field, SQLModel


class ModeOfDelivery(str, Enum):
    """Mode of delivery."""

    VAGINAL = "vaginal"
    C_SECTION = "c-section"


class HealthCareType(str, Enum):
    """Health care type."""

    PUBLIC = "public"
    INSURANCE = "insurance"
    OUT_OF_POCKET = "private"


class PlaceOfDeliveryType(str, Enum):
    """Place of birth type."""

    BIRTH_CENTER = "birth_center"
    HOSPITAL = "hospital"
    HOME = "home"
    OTHER = "other"


class Story(SQLModel, table=True):
    """Story model."""
    __tablename__ = "story"
    id: int = Field(default=None, primary_key=True)
    city: str
    country: str
    doctor: str
    doula: str
    health_care_type: HealthCareType
    midwife: str
    mode_of_delivery: ModeOfDelivery
    place_of_delivery_type: PlaceOfDeliveryType
    place_of_delivery: str = Field(max_length=100)
    rating: int = Field(ge=1, le=5)
    state: str
    summary: str
    title: str
