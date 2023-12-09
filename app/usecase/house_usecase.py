from datetime import datetime

import swisseph as swe


class HouseUsecase:
    def __init__(self, jd_utc: datetime, lat: float, lon: float) -> None:
        self.jd_utc = jd_utc
        self.lat = lat
        self.lon = lon

    def calc_house_and_ascendant(self) -> tuple[tuple[float], float]:
        swe.set_ephe_path("/Users/pineb1ue/Desktop/ast1")  # ephemerisファイルへのパスを指定
        house_positions, asmc = swe.houses(self.jd_utc, self.lat, self.lon)
        ascendant = asmc[0]
        return house_positions, ascendant
