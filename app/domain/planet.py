from enum import Enum

import swisseph as swe
from loguru import logger

from app.exceptions.exception import TopocentricCalculationError


class Planet(Enum):
    SUN = swe.SUN
    MOON = swe.MOON
    MERCURY = swe.MERCURY
    VENUS = swe.VENUS
    MARS = swe.MARS
    JUPITER = swe.JUPITER
    SATURN = swe.SATURN
    # Uranus = swe.URANUS
    # Neptune = swe.NEPTUNE
    # Pluto = swe.PLUTO

    @classmethod
    def calc_planet_positions(cls, jd_utc: float, lat: float, lon: float) -> list[float]:
        """
        Calculate planet positions based on the provided Julian date, latitude, and longitude.

        Parameters
        ----------
        jd_utc : float
            The Julian date in UTC.
        lat : float
            The latitude of the location.
        lon : float
            The longitude of the location.

        Returns
        -------
        list[float]
            A list of planet positions.
        """
        try:
            planet_positions = []
            for planet in cls:
                flag = swe.FLG_SWIEPH | swe.FLG_SPEED
                swe.set_topo(lat, lon, 0.0)
                topocentric_position, _ = swe.calc_ut(jd_utc, planet.value, flag | swe.FLG_TOPOCTR)
                planet_positions.append(float(topocentric_position[0]))
        except Exception as e:
            logger.error(e)
            raise TopocentricCalculationError()

        return planet_positions


class PlanetEmoji(Enum):
    SUN = "$☉$"
    MOON = "$☽$"
    MERCURY = "$☿$"
    VENUS = "$♀$"
    MARS = "$♂$"
    JUPITER = "$♃$"
    SATURN = "$♄$"
    # Uranus = "$♅$"
    # Neptune = "$♆$"
    # Pluto = "$♇$"

    @classmethod
    def get_names(cls) -> list[str]:
        """
        Returns a list of the names of the PlanetEmoji enum members.

        Returns
        -------
        list[str]
            List of emoji names.
        """
        return [emoji.name for emoji in cls]

    @classmethod
    def get_values(cls) -> list[str]:
        """
        Returns a list of the emoji values of the PlanetEmoji enum members.

        Returns
        -------
        list[str]
            List of emoji values.
        """
        return [emoji.value for emoji in cls]
