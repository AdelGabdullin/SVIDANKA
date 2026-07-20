"""Точка входа FastAPI-приложения «Свиданка»."""
from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="API сервиса поиска мест для свиданий",
)


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    """Проверка живости сервиса."""
    return {"status": "ok"}


# TODO: подключить роутеры из app.api.v1 по мере реализации эндпоинтов
