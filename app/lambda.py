from app import create_app
from mangum import Mangum

def handler(event, context):
    app = create_app()

    asgi_handler = Mangum(app)

    response = asgi_handler(event, context)

    print(f"ASGI Response: {response}")

    return response