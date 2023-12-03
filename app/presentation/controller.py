import pandas as pd

from app.domain.io import Request
from app.domain.planet import Planet
from app.usecase.usecase import AstrologyUsecase, TimezoneUsecase


class AstrologyController:
    def __init__(self, req: Request) -> None:
        self.req = req

        latitude: float = 36.4000
        longitude: float = 139.4600
        self.timezone_usecase = TimezoneUsecase()
        dt_utc = self.timezone_usecase.convert_to_utc_from_jst(
            self.req.yyyy,
            self.req.mm,
            self.req.dd,
            self.req.HH,
            self.req.MM,
        )
        self.astrology_usecase = AstrologyUsecase(dt_utc, latitude, longitude)

    def get_desc(self, df: pd.DataFrame) -> None:
        your_sings = self.astrology_usecase.get_all_sings()

        for planet, sign_id in zip(Planet, your_sings):
            print(df[(df["planet_id"] == planet.value) & (df["sign_id"] == sign_id)].values)
