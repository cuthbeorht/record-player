from typing import Any, Dict

from sqlalchemy.ext.asyncio import create_async_engine

from app.config import Config
from app.models import Base


class DatabaseConnection:
    """
    This will instantiate and maintain connection to the database through SQL Alchemy
    """

    def __init__(self, config: Config):
        self.config = config

        self._create_engine()

    def _create_engine(self):
        """
        Create an SQL Alchemy engine needed to connect to the database
        :return:
        """
        self.engine = create_async_engine(
            f"postgresql+asyncpg://{self.config.sql_username}:{self.config.sql_password}@{self.config.sql_host}:{self.config.sql_port}/{self.config.sql_database_name}",
            echo=True,
            future=True
        )

        print(f"Debug info: {self.engine.pool.status()}")


T = type('T')


class Repository:
    """

    """

    def find_one(self, entity: Any, filter: Dict[str, Any]) -> Any:
        raise NotImplemented
