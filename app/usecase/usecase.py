from datetime import datetime
from pathlib import Path
from typing import cast

import swisseph as swe
from domain.infra.repository import IDescBySignRepository
from domain.planet import Planet
from exception import TopocentricCalculationError
from injector import inject
from loguru import logger
from pytz import timezone


class FetchDescUsecase:
    @inject
    def __init__(self, repo: IDescBySignRepository) -> None:
        self.repo = repo

    def fetch_desc_by_signs(self, path: Path, sings: list[int]) -> None:
        df = self.repo.read_csv(path)

        desc_by_signs = []
        for planet_id, sign_id in zip(Planet, sings):
            desc_by_sign = df[(df["planet_id"] == planet_id.value) & (df["sign_id"] == sign_id)].values
            desc_by_signs.append(desc_by_sign)

        print(desc_by_signs)


class AssignUsecase:
    def __init__(
        self,
        dt: datetime,
        lat: float,
        lon: float,
    ) -> None:
        self.dt = dt
        self.lat = lat
        self.lon = lon

    def assign_sign_to_all_planets(self) -> list[int]:
        try:
            return [self._assign_sign_to_planet(planet.value) for planet in Planet]
        except Exception as e:
            logger.error(e)
            raise TopocentricCalculationError()

    def _assign_sign_to_planet(self, planet_id: int) -> int:  # TODO: intではなくPlanet?
        topocentric_position = self._calc_topocentric_position(planet_id)
        ecliptic_lon = topocentric_position[0]
        sign_id = int(ecliptic_lon // 30)
        return sign_id

    def _calc_topocentric_position(self, planet_id: int) -> list[float]:
        jd_utc = swe.julday(
            self.dt.year,
            self.dt.month,
            self.dt.day,
            self.dt.hour + self.dt.minute / 60.0 + self.dt.second / 3600.0,
        )
        flag = swe.FLG_SWIEPH | swe.FLG_SPEED
        swe.set_topo(self.lat, self.lon, 0.0)
        topocentric_position, _ = swe.calc_ut(jd_utc, planet_id, flag | swe.FLG_TOPOCTR)
        return cast(list[float], topocentric_position)


class TimezoneUsecase:
    def convert_to_utc_from_jst(
        self,
        yyyy: int,
        mm: int,
        dd: int,
        HH: int,
        MM: int,
    ) -> datetime:
        dt = datetime(yyyy, mm, dd, HH, MM, 0)
        dt_jst = dt.astimezone(timezone("Asia/Tokyo"))
        dt_utc = dt_jst.astimezone(timezone("UTC"))
        return dt_utc
