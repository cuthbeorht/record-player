from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class TodoBase(BaseModel):
    title: str
    description: Optional[str]
    created: datetime = datetime.now()
    created_by: Optional[str]


class GetTodoOutput(TodoBase):
    pass


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

    def __init__(self, database):
        """
        Creates an instance of the Recording Service class with a connection to the
        database.

        :param database:
        """
        self.db = database

    async def get_todos(self) -> List[GetTodoOutput]:
        """
        Retrieve a list of Todo items

        :return: List[Recording]
        """

        todos = [GetTodoOutput(
            **{"title": "recordings/2021-12-27_19-35-02.mp3"})]
        print(f"Todos: {todos}")

        return todos

    async def create_item(self, create_todo_request: CreateTodoInput) -> CreateTodoOutput:
        """
        Create an item to do

        :param create_todo_request:
        :return:
        """
        return CreateTodoOutput(
            title=create_todo_request.title,
            description=create_todo_request.description,
            date_created=datetime.now()
        )
