"""Конфигурация приложения через переменные окружения."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Svidanka"
    debug: bool = False

    database_url: str = "postgresql+psycopg://svidanka:svidanka@db:5432/svidanka"
    redis_url: str = "redis://redis:6379/0"
    rabbitmq_url: str = "amqp://guest:guest@rabbitmq:5672/"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
