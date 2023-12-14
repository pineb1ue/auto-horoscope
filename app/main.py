from pathlib import Path

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from loguru import logger

from app.config.logging_conf import logging_conf
from app.domain.io import Request
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


@app.post("/api/v1/horo/desc")
async def get_horoscope_descriptions(req: Request) -> JSONResponse:
    """
    Get horoscope descriptions based on astrological signs.

    Parameters
    ----------
    req : Request
        The incoming HTTP request object.

    Returns
    -------
    JSONResponse
        The HTTP response containing the horoscope descriptions as JSON.
    """
    # Log the start of the function
    logger.info(logging_conf["START"])

    # Create an instance of AstrologyController
    controller = AstrologyController()

    # Fetch horoscope descriptions based on astrological signs
    desc = controller.fetch_horoscope_descriptions(req, Path("data/desc_sign.csv"))

    # Convert the result to JSON and create an HTTP response
    res = JSONResponse(content=jsonable_encoder(desc))

    # Log the end of the function
    logger.info(logging_conf["END"])

    # Return the HTTP response
    return res


@app.post("/api/v1/horo/fig")
async def create_horoscope_figure(req: Request) -> JSONResponse:
    """
    Create a horoscope figure based on the provided request.

    Parameters
    ----------
    req : Request
        The incoming HTTP request object.

    Returns
    -------
    JSONResponse
        The HTTP response indicating the success of the operation.
    """
    # Log the start of the function
    logger.info(logging_conf["START"])

    # Create an instance of AstrologyController
    controller = AstrologyController()

    # Create a horoscope figure based on the provided request
    controller.create_and_save_horoscope(req)

    # Create an HTTP response with a success status code
    res = JSONResponse(content=None, status_code=200)

    # Log the end of the function
    logger.info(logging_conf["END"])

    # Return the HTTP response
    return res
