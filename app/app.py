from pathlib import Path

from fastapi import FastAPI

from app.domain.io import Request
from app.injector import injector
from app.presentation.controller import AstrologyController

app = FastAPI()


@app.post("/api/v1/horo/")
async def read_root(req: Request) -> None:
    controller = injector.get(AstrologyController)
    controller.fetch_desc_by_signs(req, Path("data/desc_sign.csv"))
