from pathlib import Path

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.domain.io import Request
from app.injector import injector
from app.presentation.controller import AstrologyController

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


@app.post("/api/v1/horo/sign")
async def get_desc_by_signs(req: Request) -> JSONResponse:
    controller = injector.get(AstrologyController)
    res = controller.fetch_desc_by_signs(req, Path("data/desc_sign.csv"))
    return JSONResponse(content=jsonable_encoder(res))
