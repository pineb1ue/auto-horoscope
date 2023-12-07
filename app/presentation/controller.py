from pathlib import Path
from typing import cast

from injector import inject
from loguru import logger

from app.domain.io import Request, Response, Responses
from app.domain.planet import Planet
from app.usecase.assign_sign_usecase import AssignSignUsecase
from app.usecase.fetch_desc_usecase import FetchDescUsecase
from app.usecase.timezone_usecase import TimezoneUsecase


class AstrologyController:
    @inject
    def __init__(self, fetch_desc_usecase: FetchDescUsecase) -> None:
        self.fetch_desc_usecase = fetch_desc_usecase

    def fetch_desc_by_signs(
        self,
        req: Request,
        path: Path,
        latitude: float = 36.4000,
        longitude: float = 139.4600,
    ) -> Responses:
        try:
            your_signs = self._input_your_birth_and_location(req, latitude, longitude)
            your_descriptions = self.fetch_desc_usecase.fetch_desc_by_signs(path, your_signs)

            responses = []
            for planet, your_sign, your_desc in zip(Planet, your_signs, your_descriptions):
                responses.append(Response(planet_id=planet.value, sign_id=your_sign, description=your_desc))

            return Responses(result=responses)

        except Exception as e:
            logger.error(e)
            raise

    def _input_your_birth_and_location(
        self,
        req: Request,
        latitude: float,
        longitude: float,
    ) -> list[int]:
        dt_utc = TimezoneUsecase().convert_to_utc_from_jst(req.yyyy, req.mm, req.dd, req.HH, req.MM)
        assign_sign_usecase = AssignSignUsecase(dt_utc, latitude, longitude)
        return cast(list[int], assign_sign_usecase.assign_sign_to_all_planets())
