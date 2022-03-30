import datetime
from typing import Dict, Any, List

from fastapi import Depends
from sqlalchemy import text, insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import DatabaseConnection
from app.models import Base
from app.models.todo import Todo
from sqlalchemy.orm import sessionmaker, Session


class TodoRepository:
    def __init__(self, session: AsyncSession):
        """

        """
        self.session = session

    async def find(self) -> List[Todo]:
        todos: List[Todo] = []

        cursor = await self.session.execute(select(Todo))
        results = cursor.scalars().all()

        for result in results:
            print('Results: ', result)
            todos.append(result)

        return todos

    async def add(self, entity: Any = None) -> Any:

        todo = Todo(
            title=entity.title,
            description=entity.description,
            created_by=entity.created_by,
            created=datetime.datetime.now()
        )

        # result = await session.execute(insert_stmt)
        self.session.add(todo)
        await self.session.commit()
        await self.session.refresh(todo)
        return todo
