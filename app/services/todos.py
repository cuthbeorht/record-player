from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

from app.repositories.todos import TodoRepository


class TodoBase(BaseModel):
    title: Optional[str]
    description: Optional[str]
    created: datetime = datetime.now()
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

        new_todo_item = self.repository.add(create_todo_request)

        return CreateTodoOutput(
            title=new_todo_item,
            description=create_todo_request.description,
            date_created=datetime.now()
        )
