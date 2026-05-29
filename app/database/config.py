"""Database configuration."""

from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    """Database configuration loaded from environment variables."""

    DB_SOURCE: str = (
        "postgresql+asyncpg://root:postgres@localhost:5432/birth_db"
    )
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "root"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "birth_db"
    POSTGRES_PORT: int = 5432

    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )

    @model_validator(mode="after")
    def normalize_db_source(self) -> "DatabaseSettings":
        """Ensure async driver URL for SQLAlchemy async engine."""
        if self.DB_SOURCE.startswith("postgresql://"):
            self.DB_SOURCE = self.DB_SOURCE.replace(
                "postgresql://", "postgresql+asyncpg://", 1
            )
        return self


settings = DatabaseSettings()
