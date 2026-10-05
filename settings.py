from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str

    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_environment(cls, value):
        supported = {"dev", "test", "prod"}
        if value not in supported:
            raise ValueError(f"Environment value of {value} not in {supported}")
        return value
