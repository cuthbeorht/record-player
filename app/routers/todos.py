import datetime

from fastapi import APIRouter, Depends, Response

from app.services.todos import Service as TodoService, TodoBase, CreateTodoInput
from typing import List, Any, Optional
from pydantic import BaseModel
from app.dependencies import todo_service

router = APIRouter()


class GetTodosResponse(BaseModel):
    todos: Optional[List[TodoBase]]


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
async def get_todos(todo_service: TodoService = Depends(todo_service)) -> GetTodosResponse:
    todos = await todo_service.get_todos()

    return GetTodosResponse(todos=todos.todos)


@router.post(
    "/",
    response_model=CreateTodoResponse,
    status_code=201
)
async def create_todo_item(
    request: CreateTodoRequest,
    service: TodoService = Depends(todo_service)
) -> CreateTodoResponse:

    new_todo = await service.create_item(CreateTodoInput(title=request.title, description=request.description, created_by=request.created_by))

    return CreateTodoResponse(
        id=new_todo.id,
        title=new_todo.title,
        description=new_todo.description,
        created_by=new_todo.created_by,
        created=new_todo.created
    )
