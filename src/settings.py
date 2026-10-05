from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    # Field validation can be performed also with type: Literal["dev", "test", "prod"].
    ENVIRONMENT: str
    APP_NAME: str
    API_KEY: str

    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_environment(cls, value):
        supported = {"dev", "test", "prod"}
        if value not in supported:
            raise ValueError(f"Environment value of {value} not in {supported}")
        return value
