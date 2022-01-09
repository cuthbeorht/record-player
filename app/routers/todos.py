from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
import os
from app.services.todos import Service as TodoService, Todo
from typing import List
from pydantic import BaseModel

router = APIRouter()


class GetTodosResponse(BaseModel):
    todos: List[Todo]


@router.get("/{id}")
async def get_todo_by_id(id: str):
    return {"title": "I need to do this"}



@router.get("/")
async def get_todos(todo_service: TodoService = Depends(TodoService)) -> GetTodosResponse:
    todos = await todo_service.get_todos()


    return GetTodosResponse(**{"todos": todos})
