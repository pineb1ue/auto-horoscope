from pathlib import Path

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.domain.io import Request
from app.injector import injector
from app.presentation.controller import AstrologyController

app = FastAPI()


@app.post("/api/v1/horo/")
async def get_desc_by_signs(req: Request) -> JSONResponse:
    controller = injector.get(AstrologyController)
    res = controller.fetch_desc_by_signs(req, Path("data/desc_sign.csv"))
    return JSONResponse(content=jsonable_encoder(res))
