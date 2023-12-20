from pathlib import Path

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from loguru import logger

from app.config.logging_conf import logging_conf
from app.domain.io import Request, Response, Responses
from app.domain.planet import Planet
from app.usecase.astrology_usecase import AstrologyUsecase


class AstrologyController:
    def __init__(self) -> None:
        """
        Initialize the AstrologyController.
        """
        pass

    def fetch_horoscope_descriptions(
        self,
        req: Request,
        path: Path,
        latitude: float = 36.4000,
        longitude: float = 139.4600,
    ) -> JSONResponse:
        """
        Fetch horoscope descriptions based on astrological signs.

        Parameters
        ----------
        req : Request
            The incoming HTTP request object.
        path : Path
            The path to the file containing horoscope descriptions.
        latitude : float, optional
            The latitude of the location, by default 36.4000.
        longitude : float, optional
            The longitude of the location, by default 139.4600.

        Returns
        -------
        JSONResponse
            The HTTP response containing the horoscope descriptions as JSON.
        """
        try:
            logger.info(logging_conf["START"])

            jd_utc = req.convert_to_julian_day()

            astrology_usecase = AstrologyUsecase(jd_utc, latitude, longitude)

            # Calculate signs
            your_signs = astrology_usecase.assign_signs_to_planets()
            # Generate descriptions
            your_descriptions = astrology_usecase.fetch_horoscope_descriptions(your_signs, path)

            responses = []
            for planet, your_sign, your_desc in zip(Planet, your_signs, your_descriptions):
                responses.append(Response(planet_id=planet.value, sign_id=your_sign, description=your_desc))

            logger.info(logging_conf["END"])

            # Convert the result to JSON and create an HTTP response
            return JSONResponse(content=jsonable_encoder(Responses(result=responses)))

        except Exception as e:
            logger.error(e)
            raise

    def create_and_save_horoscope(
        self,
        req: Request,
        latitude: float = 36.4000,
        longitude: float = 139.4600,
    ) -> JSONResponse:
        """
        Create a horoscope and save it to the specified path.

        Parameters
        ----------
        req : Request
            The incoming HTTP request object.
        latitude : float, optional
            The latitude of the location, by default 36.4000.
        longitude : float, optional
            The longitude of the location, by default 139.4600.

        Returns
        -------
        JSONResponse
            The HTTP response only status code.
        """
        try:
            logger.info(logging_conf["START"])

            jd_utc = req.convert_to_julian_day()
            astrology_usecase = AstrologyUsecase(jd_utc, latitude, longitude)
            astrology_usecase.create_and_save_horoscope(save_path=Path("/Users/pineb1ue/Desktop/sample.png"))

            logger.info(logging_conf["END"])

            return JSONResponse(content=None, status_code=200)

        except Exception as e:
            logger.error(e)
            raise
