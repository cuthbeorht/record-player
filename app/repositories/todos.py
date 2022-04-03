import datetime
from typing import Any, List


from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.todo import Todo


class TodoRepository:
    def __init__(self, session: AsyncSession):
        """

        """
        self.session = session

    async def find(self) -> List[Todo]:
        todos: List[Todo] = []

        cursor = await self.session.execute(select(Todo))

        for result in cursor.scalars():
            print('Results: ', result.id)
            todos.append(result)

        return todos

    async def add(self, entity: Any = None) -> Any:

        todo = Todo(
            title=entity.title,
            description=entity.description,
            created_by=entity.created_by,
            created=datetime.datetime.now()
        )

        self.session.add(todo)

        await self.session.commit()
        await self.session.refresh(todo)
        return todo
