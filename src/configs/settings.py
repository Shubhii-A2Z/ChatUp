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
    )



@lru_cache
def get_settings()->Settings:
    return Settings()