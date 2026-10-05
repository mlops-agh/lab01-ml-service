import argparse
import os
import yaml
from dotenv import load_dotenv
from settings import Settings
from pathlib import Path

CONFIG_DIR = Path("config")
SECRETS_PATH = Path("secrets.yaml")


def export_envs(environment: str = "dev") -> None:
    env_path = CONFIG_DIR / f".env.{environment}"
    if not env_path.is_file():
        raise FileNotFoundError(f"Config file not found: {env_path}")
    load_dotenv(env_path)


def export_secrets(path: Path = SECRETS_PATH) -> None:
    if not path.is_file():
        raise FileNotFoundError(f"Secrets file not found: {path}")
    with open(path, encoding="utf-8") as f:
        secrets = yaml.safe_load(f) or {}
    # An encrypted sops file always contains a top-level "sops" metadata key.
    if "sops" in secrets:
        raise RuntimeError(f"{path} is still encrypted. Run: sops -d -i {path}")
    for key, value in secrets.items():
        os.environ[str(key)] = str(value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)
    export_secrets()

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("API_KEY loaded: ", bool(settings.API_KEY))
