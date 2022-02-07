from sqlalchemy.ext.asyncio import create_async_engine

from app.config import Config


class DatabaseConnection:
    """
    This will instantiate and maintain connection to the database through SQL Alchemy
    """

    def __init__(self, config: Config):
        self.config = config

        self._create_engine()
        self._connect()

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

    def _connect(self):
        self.connection = self.engine.connect()
