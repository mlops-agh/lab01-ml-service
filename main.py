import argparse
from dotenv import load_dotenv
from settings import Settings
from pathlib import Path

CONFIG_DIR = Path("config")


def export_envs(environment: str = "dev") -> None:
    env_path = CONFIG_DIR / f".env.{environment}"
    if not env_path.is_file():
        raise FileNotFoundError(f"Config file not found: {env_path}")
    load_dotenv(env_path)


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

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
