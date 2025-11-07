from fastapi import FastAPI

from src.infrastructure.api.incident import router


def assemble_app() -> FastAPI:
    application = FastAPI()

    application.include_router(router)

    # Exception handler здесь
    # Middleware могу быть так же здесь

    return application


app = assemble_app()
