from datetime import datetime
from unittest.mock import Mock, AsyncMock

import pytest

from app.models.todo import Todo
from app.repositories.todos import TodoRepository
from app.services.todos import Service as TodoService, GetTodosOutput, TodoBase


@pytest.fixture
def todo() -> Todo:
    return Todo(
        title="title",
        description="description",
        created=datetime.now(),
        created_by="user"
    )


@pytest.mark.asyncio
async def test_given_no_todos_expect_empty_list():
    todo_repository_mock = AsyncMock(
        spec_set=TodoRepository, find=AsyncMock(return_value=[]))

    service = TodoService(todo_repository_mock)

    todos = await service.get_todos()

    assert len(todos.todos) == 0


@pytest.mark.asyncio
async def test_given_todos_expect_list_of_todos(todo: Todo):
    todo_repository_mock = AsyncMock(
        spec_set=TodoRepository, find=AsyncMock(return_value=[todo]))

    service = TodoService(todo_repository_mock)

    todos = await service.get_todos()

    assert len(todos.todos) == 1
    for item in [todo]:
        assert item == todo
