from pathlib import Path
from typing import Type

from domain.io import Request
from injector import inject
from usecase.usecase import AssignUsecase, FetchDescUsecase, TimezoneUsecase


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
    ) -> None:
        your_signs = self._input_your_birth_and_location(req, latitude, longitude)
        self.fetch_desc_usecase.fetch_desc_by_signs(path, your_signs)

    def _input_your_birth_and_location(
        self,
        req: Request,
        latitude: float,
        longitude: float,
    ) -> list[int]:
        dt_utc = TimezoneUsecase().convert_to_utc_from_jst(req.yyyy, req.mm, req.dd, req.HH, req.MM)
        assign_sign_usecase = AssignUsecase(dt_utc, latitude, longitude)
        return assign_sign_usecase.assign_sign_to_all_planets()
