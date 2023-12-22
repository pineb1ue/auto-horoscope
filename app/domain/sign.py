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
        """
        Returns a list of the names of the SignEmoji enum members.

        Returns
        -------
        list[str]
            List of emoji names.
        """
        return [emoji.name for emoji in cls]

    @classmethod
    def get_values(cls) -> list[str]:
        """
        Returns a list of the emoji values of the SignEmoji enum members.

        Returns
        -------
        list[str]
            List of emoji values.
        """
        return [emoji.value for emoji in cls]
