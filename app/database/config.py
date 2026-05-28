"""Database configuration."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    """Database configuration."""
    DB_SOURCE: str = "postgresql+asyncpg://root:pass@localhost:5432/birth_db"
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PASSWORD: str = "password"
    POSTGRES_DB: str = "birth_db"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "root"

    model_config = SettingsConfigDict(
        env_file="./.env",
        env_ignore_empty=True,
        extra="ignore",
    )


settings = DatabaseSettings()
