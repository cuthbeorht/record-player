from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Todo(BaseModel):
    title: str
    description: Optional[str]
    date_created: datetime = datetime.now()
    created_by: Optional[str]


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

    async def get_todos(self) -> List[Todo]:
        """
        Get all recordings.

        :return: List[Recording]
        """

        todos = [Todo(**{"title": "recordings/2021-12-27_19-35-02.mp3"})]
        print(f"Todos: {todos}")

        return todos
