from enum import Enum


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
