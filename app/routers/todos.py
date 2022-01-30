from fastapi import APIRouter, Depends, Response

from app.database import DatabaseConnection
from app.services.todos import Service as TodoService, TodoBase
from app.database import DatabaseConnection
from typing import List
from pydantic import BaseModel
from app.dependencies import todo_service

router = APIRouter()


class GetTodosResponse(BaseModel):
    todos: List[TodoBase]


@router.get("/{id}")
async def get_todo_by_id(id: str):
    return {"title": "I need to do this"}


@router.get("/")
async def get_todos(todo_service: TodoService = Depends(todo_service)) -> GetTodosResponse:
    todos = await todo_service.get_todos()

    return GetTodosResponse(**{"todos": todos})
