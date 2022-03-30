from typing import Any, Dict

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.config import Config
from app.models import Base

config = Config()

async_engine = create_async_engine(
    f"postgresql+asyncpg://{config.sql_username}:{config.sql_password}@{config.sql_host}:{config.sql_port}/{config.sql_database_name}",
    echo=True,
    future=True
)

async_sessionmaker = sessionmaker(
    bind=async_engine,
    future=True,
    class_=AsyncSession
)


class DatabaseConnection:
    """
    This will instantiate and maintain connection to the database through SQL Alchemy
    """

    def __init__(self, config: Config):
        self.engine = None
        self.config = config

    async def create_engine(self):
        """
        Create an SQL Alchemy engine needed to connect to the database
        :return:
        """

        self.engine = create_async_engine(
            f"postgresql+asyncpg://{self.config.sql_username}:{self.config.sql_password}@{self.config.sql_host}:{self.config.sql_port}/{self.config.sql_database_name}",
            echo=True,
            future=True
        )
