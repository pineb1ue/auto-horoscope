# from datetime import datetime

# import swisseph as swe
# from loguru import logger

# from app.domain.planet import Planet
# from app.exceptions.exception import TopocentricCalculationError


# class PlanetUsecase:
#     def __init__(self, jd_utc: datetime, lat: float, lon: float) -> None:
#         self.jd_utc = jd_utc
#         self.lat = lat
#         self.lon = lon

#     def calc_planet_positons(self) -> list[float]:
#         try:
#             return [self._calc_planet_positon(planet.value) for planet in Planet]
#         except Exception as e:
#             logger.error(e)
#             raise TopocentricCalculationError()

#     def _calc_planet_positon(self, planet_id: int) -> float:
#         flag = swe.FLG_SWIEPH | swe.FLG_SPEED
#         swe.set_topo(self.lat, self.lon, 0.0)
#         topocentric_position, _ = swe.calc_ut(self.jd_utc, planet_id, flag | swe.FLG_TOPOCTR)
#         ecliptic_lon = float(topocentric_position[0])
#         return ecliptic_lon
