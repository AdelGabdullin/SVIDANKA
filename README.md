# Свиданка (SVIDANKA)

> Веб-платформа для быстрого поиска мест для свиданий, прогулок и совместного отдыха.
> Выбираешь город, бюджет и категорию — получаешь места на карте или случайное место через режим «🎲 Кубик».

![status](https://img.shields.io/badge/status-in__development-yellow)
![python](https://img.shields.io/badge/python-3.13-blue)
![license](https://img.shields.io/badge/license-MIT-green)

## О проекте

«Свиданка» ведётся как полноценный коммерческий продукт, а не учебный pet-проект: документация пишется до кода, архитектурные решения фиксируются в ADR, код покрывается тестами, процесс идёт через GitHub Issues / Projects и CI/CD.

Подробное видение — [`docs/01_Product_Vision.md`](docs/01_Product_Vision.md).
История принятия решений (Discovery) — [`docs/meetings/product-discovery-01.md`](docs/meetings/product-discovery-01.md).

## Технологический стек

| Слой | Технологии |
|------|------------|
| Backend | Python 3.13, FastAPI, SQLAlchemy, Alembic, Pydantic |
| Хранилище | PostgreSQL, Redis |
| Очереди | RabbitMQ |
| Frontend | React, TypeScript, Leaflet |
| Инфраструктура | Docker, Docker Compose, Nginx |
| Наблюдаемость | Prometheus, Grafana |
| CI/CD | GitHub Actions |
| QA | pytest, requests, Playwright, Allure, Locust |

Обоснования — в [`docs/adr/`](docs/adr/).

## Структура репозитория

```text
SVIDANKA/
├── .github/            # CI/CD, шаблоны Issues и PR
├── docs/               # Вся документация (Vision, PRD, ADR, Test Strategy ...)
├── backend/            # FastAPI-приложение
├── frontend/           # React + TypeScript
├── infrastructure/     # Nginx, Prometheus, Grafana
├── tests/              # QA: API / UI / нагрузочные автотесты
├── scripts/            # Вспомогательные скрипты
├── docker-compose.yml
├── AGENTS.md           # Правила для ИИ-ассистентов
├── PROJECT_CONTEXT.md  # Краткий контекст проекта
└── CONTRIBUTING.md
```

## Быстрый старт (после реализации backend)

```bash
cp backend/.env.example backend/.env
docker compose up -d --build
# API:      http://localhost:8000/docs
# Frontend: http://localhost:3000
# Grafana:  http://localhost:3001
```

## Процесс разработки

- никаких коммитов напрямую в `main`;
- работа через feature-ветки (`feature/add-place-api`);
- Pull Request на каждое изменение;
- задачи — в GitHub Issues, доска — в GitHub Projects.

Подробнее — [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Лицензия

MIT — см. [`LICENSE`](LICENSE).
