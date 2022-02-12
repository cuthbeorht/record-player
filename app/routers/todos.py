import datetime

from fastapi import APIRouter, Depends, Response

from app.services.todos import Service as TodoService, TodoBase
from typing import List, Any
from pydantic import BaseModel
from app import dependencies

router = APIRouter()


class GetTodosResponse(BaseModel):
    todos: List[TodoBase]


class CreateTodoRequest(BaseModel):
    title: str
    description: str
    created_by: str
    created: Any = datetime.datetime.utcnow()


class CreateTodoResponse(BaseModel):
    id: int
    title: str
    description: str
    created_by: str
    created: Any = datetime.datetime.utcnow()


@router.get("/{id}")
async def get_todo_by_id(id: str):
    return {"title": "I need to do this"}


@router.get("/")
async def get_todos(todo_service: TodoService = Depends(dependencies.todo_service)) -> GetTodosResponse:
    todos = await todo_service.get_todos()

    return GetTodosResponse(**{"todos": todos})


@router.post(
    "/",
    response_model=CreateTodoResponse,
    status_code=201
)
async def create_todo_item(
    request: CreateTodoRequest,
    todo_service: TodoService = Depends(dependencies.todo_service)
) -> CreateTodoResponse:
    return CreateTodoResponse(
        id=1,
        title="The Title",
        description="This is a crappy description",
        created_by="skjfkj",
        created=datetime.datetime.utcnow()
    )
