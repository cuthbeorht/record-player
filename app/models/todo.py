from datetime import datetime

from sqlalchemy import Integer, Column, String, TIMESTAMP

from app.models import Base


class Todo(Base):

    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    created_by = Column(String)
    created = Column(TIMESTAMP, default=datetime.now())
