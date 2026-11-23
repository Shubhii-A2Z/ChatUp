from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import health, chat, auth, memory, threads


def create_app() -> FastAPI:
    application = FastAPI(title="ChatUp", version="0.1.0")
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.include_router(health.router)
    application.include_router(chat.router)
    application.include_router(auth.router)
    application.include_router(memory.router)
    application.include_router(threads.router)
    return application


app = create_app()


def run() -> None:
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)


if __name__=="__main__":
    run()