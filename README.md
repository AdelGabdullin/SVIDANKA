# Свиданка (SVIDANKA)

![status](https://img.shields.io/badge/status-in__development-yellow)
![python](https://img.shields.io/badge/python-3.13-blue)
![license](https://img.shields.io/badge/license-MIT-green)

## 1. Что это?

**Свиданка** — веб-платформа для быстрого поиска мест для свиданий, прогулок и совместного отдыха. Выбираешь город, бюджет и категорию — получаешь места на карте или случайное место через режим **«🎲 Кубик»**.

«Свиданка» ведётся как полноценный коммерческий продукт, а не учебный pet-проект: документация пишется до кода, архитектурные решения фиксируются в ADR, код покрывается тестами, процесс идёт через GitHub Issues / Projects и CI/CD.

## 2. Почему появился проект?

Идеи мест для свиданий и отдыха сегодня разбросаны по десяткам источников: сохранённые публикации в Instagram, Telegram-каналы, TikTok, Яндекс Карты, 2ГИС, заметки в телефоне. Информация теряется, сложно быстро найти подходящий вариант, а выбрать место случайно — вообще негде. Поиск места нередко занимает больше времени, чем сама встреча.

Подробнее — [`docs/01_Product_Vision.md`](docs/01_Product_Vision.md) и история решений в [`docs/meetings/product-discovery-01.md`](docs/meetings/product-discovery-01.md).

## 3. Основные возможности

MVP включает:

- выбор города (несколько крупных городов на старте);
- интерактивную карту и список мест;
- карточку места: фото, описание, адрес, бюджет, категории, рейтинг;
- фильтрацию по бюджету, району, расстоянию, категории;
- анонимные отзывы (просмотр и добавление, без регистрации);
- предложение нового места пользователем с постмодерацией;
- режим случайного выбора **«🎲 Кубик»**.

Полный список функциональных и нефункциональных требований — [`docs/02_PRD.md`](docs/02_PRD.md).

## 4. Технологии

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

Обоснования ключевых решений — в [`docs/adr/`](docs/adr/).

## 5. Архитектура

Backend строится на Clean Architecture с разделением по слоям (`api / services / repositories / models / schemas`), подробности — [`docs/09_System_Architecture.md`](docs/09_System_Architecture.md), доменная модель — [`docs/06_Domain_Model.md`](docs/06_Domain_Model.md), схема БД — [`docs/07_Database_Design.md`](docs/07_Database_Design.md), API — [`docs/08_API_Specification.md`](docs/08_API_Specification.md).

```text
SVIDANKA/
├── .github/            # CI/CD, шаблоны Issues и PR
├── docs/               # Вся документация (Vision, PRD, ADR, Test Strategy ...)
├── backend/            # FastAPI-приложение
├── frontend/           # React + TypeScript
├── infrastructure/      # Nginx, Prometheus, Grafana
├── tests/              # QA: API / UI / нагрузочные автотесты
├── scripts/             # Вспомогательные скрипты
├── docker-compose.yml
├── AGENTS.md           # Правила для ИИ-ассистентов
├── PROJECT_CONTEXT.md  # Краткий контекст проекта
└── CONTRIBUTING.md
```

## 6. Как запустить локально

```bash
cp backend/.env.example backend/.env
docker compose up -d --build
# API:      http://localhost:8000/docs
# Frontend: http://localhost:3000
# Grafana:  http://localhost:3001
```

> Backend и frontend пока в разработке — команда актуальна для этапа после реализации основных сервисов.

## 7. Roadmap

Этапы разработки (подробнее — [`docs/12_Roadmap.md`](docs/12_Roadmap.md)):

1. ✅ Discovery — Product Vision, PRD, User Stories, Use Cases, Business Rules.
2. ⏳ Проектирование — Domain Model, ER-диаграмма, Database Design, API Design (OpenAPI), C4-архитектура.
3. ⏳ Backend — FastAPI, PostgreSQL, SQLAlchemy, Alembic, Redis, RabbitMQ, Docker.
4. ⏳ Frontend — React + TypeScript.
5. ⏳ QA — тест-план, чек-листы, тест-кейсы, API/UI-автотесты, нагрузочное тестирование, отчёты Allure.
6. ⏳ DevOps — Docker Compose, GitHub Actions, Nginx, HTTPS, Prometheus, Grafana.

## 8. Скриншоты

_Появятся после реализации frontend._

## Процесс разработки

- никаких коммитов напрямую в `main`;
- работа через feature-ветки (`feature/add-place-api`);
- Pull Request на каждое изменение;
- задачи — в GitHub Issues, доска — в GitHub Projects.

Подробнее — [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Лицензия

MIT — см. [`LICENSE`](LICENSE).
