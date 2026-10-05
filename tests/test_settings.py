import pytest
from pydantic import ValidationError

from settings import Settings

EXPECTED_FIELDS = {"ENVIRONMENT", "APP_NAME", "API_KEY"}


@pytest.fixture
def env(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "dev")
    monkeypatch.setenv("APP_NAME", "test-app")
    monkeypatch.setenv("API_KEY", "test-key")
    return monkeypatch


def test_settings_loaded_from_environment(env):
    settings = Settings()
    assert settings.ENVIRONMENT == "dev"
    assert settings.APP_NAME == "test-app"
    assert settings.API_KEY == "test-key"


def test_settings_contain_all_expected_fields(env):
    settings = Settings()
    assert set(Settings.model_fields) == EXPECTED_FIELDS
    assert set(settings.model_dump()) == EXPECTED_FIELDS


@pytest.mark.parametrize("value", ["dev", "test", "prod"])
def test_supported_environments_accepted(env, value):
    env.setenv("ENVIRONMENT", value)
    assert Settings().ENVIRONMENT == value


def test_unsupported_environment_rejected(env):
    env.setenv("ENVIRONMENT", "staging")
    with pytest.raises(ValidationError, match="not in"):
        Settings()
