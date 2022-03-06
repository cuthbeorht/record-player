from app.database import DatabaseConnection
from app.config import Config
from fastapi import Depends

from app.repositories.todos import TodoRepository
from app.services.todos import Service as TodoService


async def database() -> DatabaseConnection:
    config = Config()
    return DatabaseConnection(config)

# Todo Related dependencies


async def todo_repository(db: DatabaseConnection = Depends(database)) -> TodoRepository:
    return TodoRepository(db)

async def todo_service(repository: TodoRepository = Depends(todo_repository)) -> TodoService:

    return TodoService(repository)



