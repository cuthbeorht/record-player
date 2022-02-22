from typing import Dict, Any

from fastapi import Depends

from app.database import DatabaseConnection, Repository


class TodoRepository(Repository):
    def __init__(self, db: DatabaseConnection):
        """

        """
        self.db = db

    def find_one(self, entity: Any, filter: Dict = None) -> Any:
        with self.db.engine.connect() as connection:
            result = connection.execute("select * from todos")

            return result
