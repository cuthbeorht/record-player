from sqlalchemy.ext.asyncio import AsyncSession

from app.database import DatabaseConnection, async_sessionmaker
from app.config import Config
from fastapi import Depends

from app.repositories.todos import TodoRepository
from app.services.todos import Service as TodoService


async def database() -> DatabaseConnection:
    config = Config()
    db = DatabaseConnection(config)
    await db.create_engine()
    return db


async def sql_session() -> AsyncSession:
    async with async_sessionmaker() as session:
        yield session


# Todo Related dependencies


async def todo_repository(db: AsyncSession = Depends(sql_session)) -> TodoRepository:
    return TodoRepository(db)


async def todo_service(repository: TodoRepository = Depends(todo_repository)) -> TodoService:
    return TodoService(repository)
