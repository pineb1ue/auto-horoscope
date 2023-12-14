from datetime import datetime
from pathlib import Path

from app.domain.planet import Planet
from app.injector.injector import injector
from app.usecase.fetch_desc_usecase import FetchDescUsecase
from app.usecase.horoscope_usecase import HoroscopeUsecase
from app.usecase.sign_usecase import SignUsecase


class AstrologyUsecase:
    def __init__(self, jd_utc: datetime, lat: float, lon: float) -> None:
        """
        Initialize the AstrologyUsecase with the given parameters.

        Parameters
        ----------
        jd_utc : datetime
            The Julian date in UTC.
        lat : float
            The latitude of the location.
        lon : float
            The longitude of the location.
        """
        self.jd_utc = jd_utc
        self.lat = lat
        self.lon = lon

        # Calculate the positions of planets
        self.planet_positions = Planet.calc_planet_positions(self.jd_utc, self.lat, self.lon)

    def create_horoscope(self, save_path: Path) -> None:
        """
        Create a horoscope and save it to the specified path.

        Parameters
        ----------
        save_path : Path
            The path where the horoscope will be saved.
        """
        horoscope_usecase = HoroscopeUsecase(self.jd_utc, self.lat, self.lon)
        horoscope_usecase.create_horoscope(self.planet_positions, save_path)

    def assign_sign_to_planets(self) -> list[int]:
        """
        Assign astrological signs to the planets based on their positions.

        Returns
        -------
        list[int]
            A list of astrological signs assigned to each planet.
        """
        return SignUsecase.assign_sign_to_planets(self.planet_positions)

    def fetch_desc_by_signs(self, signs: list[int], path: Path) -> list[str]:
        """
        Fetch horoscope descriptions based on astrological signs.

        Parameters
        ----------
        signs : list[int]
            A list of astrological signs for which descriptions will be fetched.
        path : Path
            The path to the file containing horoscope descriptions.

        Returns
        -------
        list[str]
            A list of horoscope descriptions corresponding to the provided signs.
        """
        fetch_usecase = injector.get(FetchDescUsecase)
        return fetch_usecase.fetch_desc_by_signs(signs, path)
