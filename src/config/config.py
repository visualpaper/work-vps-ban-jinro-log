from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    graphql_endpoint: str = ""
    enable_graphiql: bool = False
    logging_path: str = ""
    cookie_name: str = ""
    cookie_max_age_seconds: int = 0
    cors_allow_origin: str = ""
    mongodb_url: str = ""
    mongodb_dbname: str = ""
    mongodb_min_connection_pool: int = 0
    mongodb_max_connection_pool: int = 0

    class Config:
        env_file = ".env"


@lru_cache()
def get_config() -> Settings:
    return Settings()
