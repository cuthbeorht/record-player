from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class TodoResponse(BaseModel):
    title: str
    description: Optional[str]
    date_created: datetime = datetime.now()
    created_by: Optional[str]


class GetTodoResponse(TodoResponse):
    pass


class CreateTodoRequest(BaseModel):
    title: str
    description: str
    created_by: Optional[str]


class CreateTodoResponse(TodoResponse):
    pass


class Service:
    """
    This is the recording service.
    """

    def __init__(self, database=None):
        """
        Creates an instance of the Recording Service class with a connection to the
        database.

        :param database:
        """
        self.db = database

    async def get_todos(self) -> List[GetTodoResponse]:
        """
        Retrieve a list of Todo items

        :return: List[Recording]
        """

        todos = [GetTodoResponse(
            **{"title": "recordings/2021-12-27_19-35-02.mp3"})]
        print(f"Todos: {todos}")

        return todos

    async def create_item(self, create_todo_request: CreateTodoRequest) -> CreateTodoResponse:
        """
        Create an item to do

        :param create_todo_request:
        :return:
        """
        return CreateTodoResponse(
            title=create_todo_request.title,
            description=create_todo_request.description,
            date_created=datetime.now()
        )
