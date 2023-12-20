from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.domain.io import Request
from app.presentation.controller import AstrologyController

router = APIRouter()


@router.post("/api/v1/horo/desc")
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

    # Create an instance of AstrologyController
    controller = AstrologyController()

    # Fetch horoscope descriptions based on astrological signs
    return controller.fetch_horoscope_descriptions(req, Path("data/desc_sign.csv"))


@router.post("/api/v1/horo/fig")
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

    # Create an instance of AstrologyController
    controller = AstrologyController()

    # Return the HTTP response
    return controller.create_and_save_horoscope(req)
