from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    context_path: str = ""
    logging_path: str = ""
    cookie_name: str = ""
    cookie_max_age_seconds: int = 0
    cors_allow_origin: str = ""

    class Config:
        env_file = ".env"


@lru_cache()
def get_config() -> Settings:
    return Settings()
