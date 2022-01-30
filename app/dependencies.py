from app.database import DatabaseConnection
from app.config import Config
from fastapi import Depends
from app.services.todos import Service as TodoService


async def database() -> DatabaseConnection:
    config = Config()
    return DatabaseConnection(config)

# Todo Related dependencies


async def todo_service(database_connection: DatabaseConnection = Depends(database)) -> TodoService:

    return TodoService(database_connection)
