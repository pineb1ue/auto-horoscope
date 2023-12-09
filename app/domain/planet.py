from enum import Enum

import swisseph as swe


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
        return [emoji.name for emoji in cls]

    @classmethod
    def get_values(cls) -> list[str]:
        return [emoji.value for emoji in cls]
