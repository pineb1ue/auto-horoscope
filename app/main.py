from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.presentation.router import router

app = FastAPI()

# CORSの設定
origins = [
    "http://localhost",
    "http://localhost:5173",  # Reactの開発サーバーのポート
    "https://your-production-url",  # 本番環境のURL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
