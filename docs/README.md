

```markdown
#  backend (Flask + PostgreSQL + Nginx)

## О проекте

Backend-приложение на Python (Flask) со следующими возможностями:

- Слушает HTTP на порту 8080
- Использует PostgreSQL для хранения данных
- Nginx как обратный прокси (порт 80)

### Доступные роуты

- GET `/ping` - Проверка работы сервиса (возвращает "PONG" в HTML)
- GET `/health` - Проверка здоровья сервиса (возвращает JSON {"status": "HEALTHY"})
- GET `/list` - Список записей из БД в формате HTML
- POST `/add` - Добавление новой записи (город + температура)

### Структура базы данных
Таблица `weather`:
```sql
CREATE TABLE weather (
    city TEXT,
    temperature INT
);
```

При старте приложения автоматически добавляются тестовые данные (например: London, 20).

## Структура проекта

```
/
├── src/                  # Backend-приложение
│   ├── main.py           # Основной код FastAPI
│   └── requirements.txt  # Зависимости
├── nginx/                # Конфигурация Nginx
│   └── default.conf      
├── docker/               # Docker-конфигурации
│   ├── docker-compose.yml
│   └── Dockerfile
├── docs/                 # Документация
└── .github/              # GitHub Actions
    └── workflows/
        └── docker-build.yml
```

## Установка и запуск

1. Клонировать репозиторий:
```bash
git clone
cd <docker>
```

2. Запустить сборку и контейнеры:
```bash
docker-compose up --build
```

3. Проверить работу контейнеров:
```bash
docker ps
```

## Проверка работы

- Проверка `/ping`:
```bash
curl http://localhost/ping
```
Ожидаемый вывод: `PONG`

- Проверка `/health`:
```bash
curl http://localhost/health
```
Ожидаемый вывод: `{"status": "HEALTHY"}`

- Получить список записей:
```bash
curl http://localhost/list
```

- Добавить новую запись:
```bash
curl -X POST http://localhost/add \
  -H "Content-Type: application/json" \
  -d '{"city": "Paris", "temperature": 25}'
```

## Проверка базы данных

1. Войти в контейнер PostgreSQL:
```bash
docker exec -it <имя_postgres_контейнера> psql -U postgres (например, docker-db-1)
```

2. Выполнить запрос:
```sql
SELECT * FROM weather;
```

## GitHub Actions

Настроен автоматический пайплайн (`.github/workflows/docker-build.yml`), который:
- Запускается при пуше в ветку `main`
- Собирает Docker-образы и выводит логи по сборке

## Контакты

По вопросам обращайтесь: [hsdfwert@gmail.com](mailto:hsdfwert@gmail.com)

```
https://git.miem.hse.ru/blank1330108
