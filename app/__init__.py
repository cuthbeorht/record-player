from fastapi import FastAPI
from app.routers.health import router as health_router
from app.routers.todos import router as todo_router


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(health_router, prefix="/health")
    app.include_router(todo_router, prefix="/todos")

    return app
