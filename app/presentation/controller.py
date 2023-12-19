from pathlib import Path

from loguru import logger

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
    ) -> Responses:
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
        Responses
            The HTTP response containing the horoscope descriptions as JSON.
        """
        try:
            jd_utc = req.convert_to_julian_day()

            astrology_usecase = AstrologyUsecase(jd_utc, latitude, longitude)

            # Calculate signs
            your_signs = astrology_usecase.assign_signs_to_planets()
            # Generate descriptions
            your_descriptions = astrology_usecase.fetch_horoscope_descriptions(your_signs, path)

            responses = []
            for planet, your_sign, your_desc in zip(Planet, your_signs, your_descriptions):
                responses.append(Response(planet_id=planet.value, sign_id=your_sign, description=your_desc))

            return Responses(result=responses)

        except Exception as e:
            logger.error(e)
            raise

    def create_and_save_horoscope(
        self,
        req: Request,
        latitude: float = 36.4000,
        longitude: float = 139.4600,
    ) -> None:
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
        """
        try:
            jd_utc = req.convert_to_julian_day()
            astrology_usecase = AstrologyUsecase(jd_utc, latitude, longitude)
            astrology_usecase.create_and_save_horoscope(save_path=Path("/Users/pineb1ue/Desktop/sample.png"))

        except Exception as e:
            logger.error(e)
            raise
