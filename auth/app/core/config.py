from typing import List
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False, extra="ignore"
    )

    # App Settings
    app_name: str = "FastAPI Auth Backend"
    version: str = "0.1.0"
    environment: str = Field(default="development", alias="ENVIRONMENT")
    debug: bool = Field(default=True, alias="DEBUG")

    # Database
    database_url: str = Field(alias="DATABASE_URL")
    async_database_url: str = Field(alias="ASYNC_DATABASE_URL")
    db_pool_size: int = Field(default=5, alias="DB_POOL_SIZE")
    db_max_overflow: int = Field(default=10, alias="DB_MAX_OVERFLOW")

    # Security
    secret_key: str = Field(alias="SECRET_KEY")
    algorithm: str = Field(default="HS256", alias="ALGORITHM")
    access_token_expire_minutes: int = Field(
        default=30, alias="ACCESS_TOKEN_EXPIRE_MINUTES"
    )

    # CORS
    allowed_hosts: List[str] = Field(
        default=["localhost", "127.0.0.1"], alias="ALLOWED_HOSTS"
    )
    cors_origins: List[str] = Field(
        default=["http://localhost:3000", "http://localhost:8000"], alias="CORS_ORIGINS"
    )


settings = Settings()
