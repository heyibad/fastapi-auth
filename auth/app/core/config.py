from typing import List
from pydantic import Field, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict
import secrets

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8", 
        case_sensitive=False, 
        extra="ignore"
    )

    # App Settings
    app_name: str = "FastAPI Auth Backend"
    version: str = "0.1.0"
    environment: str = Field(default="development", alias="ENVIRONMENT")
    debug: bool = Field(default=True, alias="DEBUG")

    # Database - with fallbacks for development
    database_url: str = Field(
        default="sqlite:///./app.db", 
        alias="DATABASE_URL",
        description="Database connection URL"
    )
    async_database_url: str = Field(
        default="sqlite+aiosqlite:///./app.db", 
        alias="ASYNC_DATABASE_URL",
        description="Async database connection URL"
    )
    db_pool_size: int = Field(default=5, alias="DB_POOL_SIZE")
    db_max_overflow: int = Field(default=10, alias="DB_MAX_OVERFLOW")

    # Security - generate random secret if not provided
    secret_key: str = Field(
        default_factory=lambda: secrets.token_urlsafe(32), 
        alias="SECRET_KEY",
        description="Secret key for JWT token signing"
    )
    algorithm: str = Field(default="HS256", alias="ALGORITHM")
    access_token_expire_minutes: int = Field(
        default=30, alias="ACCESS_TOKEN_EXPIRE_MINUTES"
    )

    # CORS
    allowed_hosts: List[str] = Field(
        default=["localhost", "127.0.0.1"], alias="ALLOWED_HOSTS"
    )
    cors_origins: List[str] = Field(
        default=["http://localhost:3000", "http://localhost:8000"], 
        alias="CORS_ORIGINS"
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Warn if using default secret key in production
        if self.environment == "production" and self.secret_key.startswith("fallback"):
            raise ValueError("SECRET_KEY must be set in production environment!")

# Create settings instance
try:
    settings = Settings()
except ValidationError as e:
    print(f"Configuration error: {e}")
    print("Please check your .env file or environment variables")
    raise