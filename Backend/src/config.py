from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    """
    Base configuration class which loads environment variables from .env files.
    """

    model_config = SettingsConfigDict(
        env_file=(
            "envs/backend.env",
            "envs/pg.env",
        ),
    )


class PostgresConfig(BaseConfig):
    POSTGRES_URL: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str




class JwtConfig(BaseConfig):
    SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_EXPIRATION_MINUETS: int
    CODE_EXPIRATION_MINUTES : int


class MailConfig(BaseConfig):
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: str
    MAIL_SERVER: str
    MAIL_FROM_NAME: str

class RedisConfig(BaseConfig):
    REDIS_URL : str


class Settings(
    PostgresConfig,
    JwtConfig,
    MailConfig,
    RedisConfig,
):
    pass


settings: Settings = Settings()