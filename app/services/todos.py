from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

from app.repositories.todos import TodoRepository


class TodoBase(BaseModel):
    id: Optional[int]
    title: Optional[str]
    description: Optional[str]
    created: Optional[datetime]
    created_by: Optional[str]


class GetTodosOutput(TodoBase):
    todos: List[TodoBase]


class CreateTodoInput(BaseModel):
    title: str
    description: str
    created_by: Optional[str]


class CreateTodoOutput(TodoBase):
    pass


class Service:
    """
    This is the recording service.
    """

    def __init__(self, repository: TodoRepository):
        """
        Creates an instance of the Recording Service class with a connection to the
        database.

        :param database:
        """
        self.repository = repository

    async def get_todos(self) -> GetTodosOutput:
        """
        Retrieve a list of Todo items

        :return: List[Recording]
        """

        todos_output: List[TodoBase] = []

        todos = await self.repository.find()
        for todo in todos:
            todos_output.append(TodoBase(
                id=todo.id,
                title=todo.title,
                description=todo.description,
                created_by=todo.created_by,
                created=todo.created
            ))

        return GetTodosOutput(todos=todos_output)

    async def create_item(self, create_todo_request: CreateTodoInput) -> CreateTodoOutput:
        """
        Create an item to do

        :param create_todo_request:
        :return:
        """

        new_todo_item = await self.repository.add(create_todo_request)

        return CreateTodoOutput(
            id=new_todo_item.id,
            created_by=new_todo_item.created_by,
            title=new_todo_item.title,
            description=create_todo_request.description,
            date_created=datetime.now()
        )
