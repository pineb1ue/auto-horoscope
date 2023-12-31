import swisseph as swe
from loguru import logger


class HouseUsecase:
    def __init__(self) -> None:
        pass

    def calc_house_positions_and_ascendant(self, jd_utc: float, lat: float, lon: float) -> tuple[tuple[float], float]:
        logger.info("Start HouseUsecase")

        # Set the path to the ephemeris file
        swe.set_ephe_path("/Users/pineb1ue/Desktop/ast1")

        # Calculate house positions and ascendant
        house_positions, asmc = swe.houses(jd_utc, lat, lon)

        # Extract the ascendant from the result
        ascendant = asmc[0]

        logger.info("End HouseUsecase")

        return house_positions, ascendant
