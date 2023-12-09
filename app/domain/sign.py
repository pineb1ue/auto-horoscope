from enum import Enum


class Sign(Enum):
    ARIES = 0
    TAURUS = 1
    GEMINI = 2
    CANCER = 3
    LEO = 4
    VIRGO = 5
    LIBRA = 6
    SCORPIO = 7
    SAGITTARIUS = 8
    CAPRICORN = 9
    AQUARIUS = 10
    PISCES = 11


class SignEmoji(Enum):
    ARIES = "♈"
    TAURUS = "♉"
    GEMINI = "♊"
    CANCER = "♋"
    LEO = "♌"
    VIRGO = "♍"
    LIBRA = "♎"
    SCORPIO = "♏"
    SAGITTARIUS = "♐"
    CAPRICORN = "♑"
    AQUARIUS = "♒"
    PISCES = "♓"

    @classmethod
    def get_names(cls) -> list[str]:
        return [emoji.name for emoji in cls]

    @classmethod
    def get_values(cls) -> list[str]:
        return [emoji.value for emoji in cls]
