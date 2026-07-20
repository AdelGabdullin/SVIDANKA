# AGENTS.md

Инструкция для ИИ-ассистентов (Codex, Claude и т.п.), работающих в этом репозитории.

## Project
Название: Свиданка (SVIDANKA)

## Stack
- Python 3.13
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Redis
- RabbitMQ
- React + TypeScript
- Docker

## Code Style
- Ruff
- Black
- mypy
- Conventional Commits

## Architecture
- Clean Architecture
- Feature-based структура (api / services / repositories / models / schemas)

## Principles
- Не писать код без тестов.
- Всегда использовать type hints.
- Все изменения сопровождаются документацией.
- Не использовать магические числа.
- Все API документируются через OpenAPI.

## AI Development Rules
Перед изменением кода:
1. Изучить `PROJECT_CONTEXT.md` и `docs/01_Product_Vision.md`.
2. Проверить существующую архитектуру и не ломать текущий функционал.
3. Не вводить новые технологии без обсуждения и без записи ADR.
4. Придерживаться порядка документов: Vision → PRD → User Stories → Use Cases → Domain Model → Database Design → Architecture → Code.
