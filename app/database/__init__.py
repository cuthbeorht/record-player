from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.config import Config

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
