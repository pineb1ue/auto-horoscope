from datetime import datetime

import swisseph as swe


class HouseUsecase:
    def __init__(self, jd_utc: datetime, lat: float, lon: float) -> None:
        """
        Initialize the HouseUsecase with the given parameters.

        Parameters
        ----------
        jd_utc : datetime
            Julian Date in UTC.
        lat : float
            Latitude of the location.
        lon : float
            Longitude of the location.
        """
        self.jd_utc = jd_utc
        self.lat = lat
        self.lon = lon

    def calc_house_positions_and_ascendant(self) -> tuple[tuple[float], float]:
        """
        Calculate house positions and ascendant based on the provided parameters.

        Returns
        -------
        tuple[tuple[float], float]
            A tuple containing house positions (as a tuple) and ascendant.
        """
        # Set the path to the ephemeris file
        swe.set_ephe_path("/Users/pineb1ue/Desktop/ast1")

        # Calculate house positions and ascendant
        house_positions, asmc = swe.houses(self.jd_utc, self.lat, self.lon)

        # Extract the ascendant from the result
        ascendant = asmc[0]

        return house_positions, ascendant
