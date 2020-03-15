создание файла миграции для автоматического изменения схемы:

```alembic revision --autogenerate -m "add users"```

применение новых файлов миграций к схеме:

```alembic upgrade head```
