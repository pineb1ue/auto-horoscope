from datetime import datetime
from typing import cast

import swisseph as swe
from loguru import logger

from app.domain.planet import Planet
from app.exceptions.exception import TopocentricCalculationError


class AssignSignUsecase:
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

    def calc_planet_positons(self) -> list[float]:
        try:
            return [self._calc_planet_positon(planet.value) for planet in Planet]
        except Exception as e:
            logger.error(e)
            raise TopocentricCalculationError()

    def _assign_sign_to_planet(self, planet_id: int) -> int:  # TODO: intではなくPlanet?
        ecliptic_lon = self._calc_planet_positon(planet_id)
        sign_id = int(ecliptic_lon // 30)
        return sign_id

    def _calc_planet_positon(self, planet_id: int) -> float:
        topocentric_position = self._calc_topocentric_position(planet_id)
        ecliptic_lon = topocentric_position[0]
        return ecliptic_lon

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
