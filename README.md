# Как запустить
```bash
cp env.example .env
```

Написать в одну переменную какое-то названия, оно будет названием для базы sqlite

```bash
python3.12 -m venv venv
. venv/bin/activate
alembic upgrade heads
uvicorn src:app --port 8000
```

Зайти на http://localhost:8000/docs

# Примеры эндпоинтов
## GET /incident
Список инцидентов, опционально можно прислать status, по нему будет фильтр. В идеале стоит добавить пагинацию, когда их будет много.

Поиск идет через ilike.

```bash
curl \
  'http://localhost:8000/incident' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
```

Ответ 200:
```json
[
    {
        "id": 1,
        "text": "o",
        "description": "test",
        "status": "b",
        "source": "z",
        "created_at": "2025-11-07T09:19:28"
    },
    {
        "id": 2,
        "text": "ucar<>topdoer",
        "description": "testovoe zadanie",
        "status": "test_status",
        "source": "manager Andrey",
        "created_at": "2025-11-07T15:48:58"
    }
]
```

Запрос с фильтром по статусу
```bash
curl \
  'http://localhost:8000/incident?status=test' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
```

Ответ 200:
```json
[
    {
        "id": 2,
        "text": "ucar<>topdoer",
        "description": "testovoe zadanie",
        "status": "test_status",
        "source": "manager Andrey",
        "created_at": "2025-11-07T15:48:58"
    }
]
```

## POST /incident
Создает инцидент, в теле прислать все параметры.

```bash
curl -X 'POST' \
  'http://localhost:8000/incident' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "ucar<>topdoer",
  "description": "testovoe zadanie",
  "status": "partner",
  "source": "manager Andrey"
}'
```

Ответ 200:
```json
{
    "id":2,
    "text":"ucar<>topdoer",
    "description":"testovoe zadanie",
    "status":"partner",
    "source":"manager Andrey",
    "created_at":"2025-11-07T15:48:58"
}
```

## PATCH /incident
Обновляет статус инцидента, новый статус присылается в теле.

```bash
curl -X 'PATCH' \
  'http://localhost:8000/incident/2' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "status": "test_status"
  }'
```

Ответ 200:
```json
{
    "id":2,
    "text":"ucar<>topdoer",
    "description":"testovoe zadanie",
    "status":"test_status",
    "source":"manager Andrey",
    "created_at":"2025-11-07T15:48:58"
}
```
