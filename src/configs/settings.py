from functools import lru_cache
from pydantic_settings import SettingsConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Env settings for the application
    Automatically reads configurations from environment variables and validate them at runtime.
    """

    # Loading the configs from .env file
    model_config=SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    postgres_user: str="chatup"
    postgres_password: str="chatup"
    postgres_db: str="chatup"
    postgres_host: str="localhost"
    postgres_port: str="5432"

    database_url: str

    postgres_pool_min_size: int=1 # Minimum number of connections to keep open
    postgres_pool_max_size: int=8 # Maximum number of connections to keep open
    postgres_pool_open: bool=True # Whether to open connection pool
    postgres_row_factory: str="dict" # Type of row factory to use for queries to return results

    groq_api_key: str=""
    chat_model: str=""
    memory_model: str=""

    @property
    def database_url(self)->str:
        return (
            f"postgresql://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}"
            f"/{self.postgres_db}"
        )


@lru_cache
def get_settings()->Settings:
    return Settings()