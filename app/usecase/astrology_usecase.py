from datetime import datetime
from pathlib import Path

from app.domain.planet import Planet
from app.injector.injector import injector
from app.usecase.fetch_desc_usecase import FetchDescUsecase
from app.usecase.horoscope_usecase import HoroscopeUsecase
from app.usecase.sign_usecase import SignUsecase


class AstrologyUsecase:
    def __init__(self, jd_utc: datetime, lat: float, lon: float) -> None:
        self.jd_utc = jd_utc
        self.lat = lat
        self.lon = lon

        # 惑星の位置を計算
        self.planet_positions = Planet.calc_planet_positons(self.jd_utc, self.lat, self.lon)

    def create_horoscope(self, save_path: Path) -> None:
        horoscope_usecase = HoroscopeUsecase(self.jd_utc, self.lat, self.lon)
        horoscope_usecase.create_horoscope(self.planet_positions, save_path)

    def assign_sign_to_planets(self) -> list[int]:
        return SignUsecase.assign_sign_to_planets(self.planet_positions)

    def fetch_desc_by_signs(self, signs: list[int], path: Path) -> list[str]:
        fetch_usecase = injector.get(FetchDescUsecase)
        return fetch_usecase.fetch_desc_by_signs(signs, path)
