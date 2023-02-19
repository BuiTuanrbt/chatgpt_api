# configs.py
from pathlib import Path
from typing import Optional, List

from pydantic import BaseSettings, Field, BaseModel


class AppConfig(BaseModel):
    """Application configurations."""

    # all the directory level information defined at app config level
    # we do not want to pollute the env level config with these information
    # this can change on the basis of usage

    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent

    SETTINGS_DIR: Path = BASE_DIR.joinpath('settings')
    SETTINGS_DIR.mkdir(parents=True, exist_ok=True)

    LOGS_DIR: Path = BASE_DIR.joinpath('logs')
    LOGS_DIR.mkdir(parents=True, exist_ok=True)

    DOMAIN_PATH: Path = BASE_DIR.joinpath('domain')


class GlobalConfig(BaseSettings):
    """Global configurations."""

    # These variables will be loaded from the .env file. However, if
    # there is a shell environment variable having the same name,
    # that will take precedence.

    APP_CONFIG: AppConfig = AppConfig()

    API_NAME: Optional[str] = Field(None, env="API_NAME")
    API_DESCRIPTION: Optional[str] = Field(None, env="API_DESCRIPTION")
    API_VERSION: Optional[str] = Field(None, env="API_VERSION")
    API_DEBUG_MODE: Optional[bool] = Field(None, env="API_DEBUG_MODE")
    SSL: Optional[str] = Field(None, env="SSL")

    # define global variables with the Field class
    ENV_STATE: Optional[str] = Field(None, env="ENV_STATE")

    # logging configuration file
    LOG_CONFIG_FILENAME: Optional[str] = Field(None, env="LOG_CONFIG_FILENAME")

    # environment specific variables do not need the Field class
    HOST: Optional[str] = None
    PORT: Optional[int] = None
    LOG_LEVEL: Optional[str] = None

    DB: Optional[str] = None

    ALLOWED_HOSTS: List[str] = Field(None, env="ALLOWED_HOSTS")

    class Config:
        """Loads the dotenv file."""

        env_file: str = ".env"
        env_prefix: str = "DEV_"

    # Get Minio Config
    MINIO_HOST: Optional[str] = Field(
        None, env=Config.env_prefix + 'MINIO_HOST')
    MINIO_ACCESS_KEY: Optional[str] = Field(
        None, env=Config.env_prefix + 'MINIO_ACCESS_KEY')
    MINIO_SECRET_KEY: Optional[str] = Field(
        None, env=Config.env_prefix + 'MINIO_SECRET_KEY')
    MINIO_SECURE: Optional[bool] = Field(
        None, env=Config.env_prefix + 'MINIO_SECURE')

    # Get ElasticSearch Config
    ELASTICSEARCH_HOST: Optional[str] = Field(
        None, env=Config.env_prefix + 'ELASTICSEARCH_HOST')
    ELASTICSEARCH_PORT: Optional[str] = Field(
        None, env=Config.env_prefix + 'ELASTICSEARCH_PORT')
    ELASTICSEARCH_INDEX: Optional[str] = Field(
        None, env=Config.env_prefix + 'ELASTICSEARCH_INDEX')
    ELASTICSEARCH_USERNAME: Optional[str] = Field(
        None, env=Config.env_prefix + 'ELASTICSEARCH_USERNAME')
    ELASTICSEARCH_PASSWORD: Optional[str] = Field(
        None, env=Config.env_prefix + 'ELASTICSEARCH_PASSWORD')

    # Score Config
    SCORE: Optional[int] = Field(None, env='SCORE')


class DevConfig(GlobalConfig):
    """Development configurations."""

    class Config:
        env_prefix: str = "DEV_"

    MINIO_HOST: Optional[str] = Field(
        None, env=Config.env_prefix + 'MINIO_HOST')
    MINIO_ACCESS_KEY: Optional[str] = Field(
        None, env=Config.env_prefix + 'MINIO_ACCESS_KEY')
    MINIO_SECRET_KEY: Optional[str] = Field(
        None, env=Config.env_prefix + 'MINIO_SECRET_KEY')
    MINIO_SECURE: Optional[bool] = Field(
        None, env=Config.env_prefix + 'MINIO_SECURE')

    # Get ElasticSearch Config
    ELASTICSEARCH_HOST: Optional[str] = Field(
        None, env=Config.env_prefix + 'ELASTICSEARCH_HOST')
    ELASTICSEARCH_PORT: Optional[str] = Field(
        None, env=Config.env_prefix + 'ELASTICSEARCH_PORT')
    ELASTICSEARCH_INDEX: Optional[str] = Field(
        None, env=Config.env_prefix + 'ELASTICSEARCH_INDEX')
    ELASTICSEARCH_USERNAME: Optional[str] = Field(
        None, env=Config.env_prefix + 'ELASTICSEARCH_USERNAME')
    ELASTICSEARCH_PASSWORD: Optional[str] = Field(
        None, env=Config.env_prefix + 'ELASTICSEARCH_PASSWORD')
    ES_CLUSTER: List[str] = Field(None, env=Config.env_prefix + 'ES_CLUSTER')


class SITConfig(GlobalConfig):
    """SIT configurations."""

    class Config:
        env_prefix: str = "SIT_"

    MINIO_HOST: Optional[str] = Field(
        None, env=Config.env_prefix + 'MINIO_HOST')
    MINIO_ACCESS_KEY: Optional[str] = Field(
        None, env=Config.env_prefix + 'MINIO_ACCESS_KEY')
    MINIO_SECRET_KEY: Optional[str] = Field(
        None, env=Config.env_prefix + 'MINIO_SECRET_KEY')
    MINIO_SECURE: Optional[bool] = Field(
        None, env=Config.env_prefix + 'MINIO_SECURE')

    # Get ElasticSearch Config
    ELASTICSEARCH_HOST: Optional[str] = Field(
        None, env=Config.env_prefix + 'ELASTICSEARCH_HOST')
    ELASTICSEARCH_PORT: Optional[str] = Field(
        None, env=Config.env_prefix + 'ELASTICSEARCH_PORT')
    ELASTICSEARCH_INDEX: Optional[str] = Field(
        None, env=Config.env_prefix + 'ELASTICSEARCH_INDEX')
    ELASTICSEARCH_USERNAME: Optional[str] = Field(
        None, env=Config.env_prefix + 'ELASTICSEARCH_USERNAME')
    ELASTICSEARCH_PASSWORD: Optional[str] = Field(
        None, env=Config.env_prefix + 'ELASTICSEARCH_PASSWORD')
    ES_CLUSTER: List[str] = Field(None, env=Config.env_prefix + 'ES_CLUSTER')


class UATConfig(GlobalConfig):
    """UAT configurations."""

    class Config:
        env_prefix: str = "UAT_"

    MINIO_HOST: Optional[str] = Field(
        None, env=Config.env_prefix + 'MINIO_HOST')
    MINIO_ACCESS_KEY: Optional[str] = Field(
        None, env=Config.env_prefix + 'MINIO_ACCESS_KEY')
    MINIO_SECRET_KEY: Optional[str] = Field(
        None, env=Config.env_prefix + 'MINIO_SECRET_KEY')
    MINIO_SECURE: Optional[bool] = Field(
        None, env=Config.env_prefix + 'MINIO_SECURE')

    # Get ElasticSearch Config
    ELASTICSEARCH_HOST: Optional[str] = Field(
        None, env=Config.env_prefix + 'ELASTICSEARCH_HOST')
    ELASTICSEARCH_PORT: Optional[str] = Field(
        None, env=Config.env_prefix + 'ELASTICSEARCH_PORT')
    ELASTICSEARCH_INDEX: Optional[str] = Field(
        None, env=Config.env_prefix + 'ELASTICSEARCH_INDEX')
    ELASTICSEARCH_USERNAME: Optional[str] = Field(
        None, env=Config.env_prefix + 'ELASTICSEARCH_USERNAME')
    ELASTICSEARCH_PASSWORD: Optional[str] = Field(
        None, env=Config.env_prefix + 'ELASTICSEARCH_PASSWORD')
    ES_CLUSTER: List[str] = Field(None, env=Config.env_prefix + 'ES_CLUSTER')


class ProdConfig(GlobalConfig):
    """Production configurations."""

    class Config:
        env_prefix: str = "PROD_"

    MINIO_HOST: Optional[str] = Field(
        None, env=Config.env_prefix + 'MINIO_HOST')
    MINIO_ACCESS_KEY: Optional[str] = Field(
        None, env=Config.env_prefix + 'MINIO_ACCESS_KEY')
    MINIO_SECRET_KEY: Optional[str] = Field(
        None, env=Config.env_prefix + 'MINIO_SECRET_KEY')
    MINIO_SECURE: Optional[bool] = Field(
        None, env=Config.env_prefix + 'MINIO_SECURE')

    # Get ElasticSearch Config
    ELASTICSEARCH_HOST: Optional[str] = Field(
        None, env=Config.env_prefix + 'ELASTICSEARCH_HOST')
    ELASTICSEARCH_PORT: Optional[str] = Field(
        None, env=Config.env_prefix + 'ELASTICSEARCH_PORT')
    ELASTICSEARCH_INDEX: Optional[str] = Field(
        None, env=Config.env_prefix + 'ELASTICSEARCH_INDEX')
    ELASTICSEARCH_USERNAME: Optional[str] = Field(
        None, env=Config.env_prefix + 'ELASTICSEARCH_USERNAME')
    ELASTICSEARCH_PASSWORD: Optional[str] = Field(
        None, env=Config.env_prefix + 'ELASTICSEARCH_PASSWORD')

    ES_CLUSTER: List[str] = Field(None, env=Config.env_prefix + 'ES_CLUSTER')


class FactoryConfig:
    """Returns a config instance depending on the ENV_STATE variable."""

    def __init__(self, env_state: Optional[str]):
        self.env_state = env_state

    def __call__(self):
        if self.env_state == "dev":
            return DevConfig()

        elif self.env_state == "prod":
            return ProdConfig()

        elif self.env_state == "sit":
            return SITConfig()

        elif self.env_state == "uat":
            return UATConfig()


settings = FactoryConfig(GlobalConfig().ENV_STATE)()
# print(settings.MINIO_HOST)
print(settings.ENV_STATE)
# print(settings.__repr__())
