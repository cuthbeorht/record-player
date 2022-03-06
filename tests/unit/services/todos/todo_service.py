from datetime import datetime
from unittest.mock import Mock

import pytest

from app.repositories.todos import TodoRepository
from app.services.todos import GetTodoOutput
from app.services.todos import Service as TodoService

@pytest.mark.asyncio
async def test_get_todos():
    todo_repository_mock = Mock(spec_set=TodoRepository, find_one=GetTodoOutput(
        title="title", descriptoin="description", created=datetime.now(), created_by="user"))

    service = TodoService(todo_repository_mock)

    todos = await service.get_todos()

    assert len(todos) > 0
