import json
from typing import Dict, Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from app.routers.health import router as health_router
from app.routers.todos import router as todo_router


def create_app() -> FastAPI:
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_methods=['*'],
        allow_headers=['*'],
        allow_credentials=True
    )

    app.include_router(health_router, prefix="/health")
    app.include_router(todo_router, prefix="/todos")

    schema = _generate_openapi(app=app)
    _persist_openapi_schema(schema)

    return app


def _generate_openapi(app: FastAPI) -> Dict[str, Any]:
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Todo OpenApi",
        version="0.0.1",
        description="This is the basic Swagger UI Open Api docs",
        routes=app.routes
    )

    app.openapi_schema = openapi_schema

    return app.openapi_schema


def _persist_openapi_schema(schema) -> None:
    with open('openapi.json', 'w') as f:
        f.write(json.dumps(schema))
