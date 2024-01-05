from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.domain.container import Container
from app.presentation.endpoint import router


def create_app() -> FastAPI:
    container = Container()

    # CORSの設定
    origins = [
        "http://localhost",
        "http://localhost:5173",  # Reactの開発サーバーのポート
        "https://your-production-url",  # 本番環境のURL
    ]

    app = FastAPI()
    app.container = container  # type: ignore[attr-defined]
    app.include_router(router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app


app = create_app()
