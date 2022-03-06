from typing import Dict, Any, List

from fastapi import Depends
from sqlalchemy import text, insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import DatabaseConnection, Repository
from app.models.todo import Todo
from sqlalchemy.orm import sessionmaker, Session


class TodoRepository(Repository):
    def __init__(self, db: DatabaseConnection):
        """

        """
        self.db = db
        self._instantiate_session()

    def _instantiate_session(self):
        self.session_factory = sessionmaker(
            bind=self.db.engine, class_=AsyncSession)

    async def find(self, entity: Todo = None, filter: Dict = None) -> List[Todo]:

        todos: List[Todo] = []

        async with self.session_factory() as session:
            query = select(Todo)
            r = await session.execute(query)
            cursor = r.scalars()

        for result in cursor:
            todos.append(result)

        return todos

    async def add(self, entity: Any = None) -> Any:
        async with self.db.engine.begin() as conn:
            result = await conn.execute(insert(entity))
