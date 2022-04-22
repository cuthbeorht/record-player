from typing import Any
from unittest.mock import Mock, AsyncMock

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.todo import Todo
from app.repositories.todos import TodoRepository


@pytest.fixture()
def todos():
    return [Todo(id=1, title='foo', description='bar')]


@pytest.fixture()
def cursor_stub(todos):
    class CursorStub:
        def scalars(self):
            return todos

    return CursorStub()


@pytest.fixture()
def cursor_stub_empty():
    class CursorStub:

        def scalars(self):
            return []

    return CursorStub()


@pytest.fixture()
def session_stub(cursor_stub):
    class SessionStub:

        def __init__(self,  **kw):
            super().__init__(**kw)
            self.cursor = cursor_stub

        @classmethod
        def _regenerate_proxy_for_target(cls, target):
            pass

        async def execute(self, statement: Any):
            return self.cursor

    return SessionStub()


@pytest.fixture()
def session_stub_empty(cursor_stub_empty):
    class SessionStub:

        def __init__(self,  **kw):
            super().__init__(**kw)
            self.cursor = cursor_stub_empty

        @classmethod
        def _regenerate_proxy_for_target(cls, target):
            pass

        async def execute(self, statement: Any):
            return self.cursor

    return SessionStub()


@pytest.mark.asyncio
async def test_given_todos_find_should_return_todo_items(
    session_stub,
    todos
):
    repo = TodoRepository(session_stub)

    result = await repo.find()

    assert result == todos


@pytest.mark.asyncio
async def test_given_no_todos_find_should_return_empty_list(
    session_stub_empty
):
    repo = TodoRepository(session_stub_empty)

    result = await repo.find()

    assert result == []
