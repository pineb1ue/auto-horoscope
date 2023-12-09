from pathlib import Path

from injector import inject
from loguru import logger

from app.domain.io import Request, Response, Responses
from app.domain.planet import Planet
from app.usecase.fetch_desc_usecase import FetchDescUsecase
from app.usecase.house_usecase import HouseUsecase
from app.usecase.planet_usecase import PlanetUsecase
from app.usecase.sign_usecase import SignUsecase
from app.usecase.time_usecase import TimeUsecase


class AstrologyController:
    @inject
    def __init__(self, fetch_desc_usecase: FetchDescUsecase) -> None:
        self.fetch_desc_usecase = fetch_desc_usecase

    def fetch_desc_by_signs(
        self,
        req: Request,
        path: Path,
        latitude: float = 36.4000,
        longitude: float = 139.4600,
    ) -> Responses:
        try:
            # ユリウス日(UTC)の計算
            jd_utc = TimeUsecase.convert_to_julian_day(req.yyyy, req.mm, req.dd, req.HH, req.MM)

            planet_usecase = PlanetUsecase(jd_utc, latitude, longitude)
            sign_usecase = SignUsecase()
            house_usecase = HouseUsecase(jd_utc, latitude, longitude)

            # 惑星の位置を計算
            your_planet_positions = planet_usecase.calc_planet_positons()

            # サインの計算, 文章作成
            your_signs = sign_usecase.assign_sign_to_all_planets(your_planet_positions)
            your_descriptions = self.fetch_desc_usecase.fetch_desc_by_signs(path, your_signs)

            # ハウスの計算, ホロスコープ作成
            your_houses, your_ascendant = house_usecase.calc_house_and_ascendant()
            house_usecase.draw_horoscope_chart(your_ascendant, your_planet_positions, your_houses)

            responses = []
            for planet, your_sign, your_desc in zip(Planet, your_signs, your_descriptions):
                responses.append(Response(planet_id=planet.value, sign_id=your_sign, description=your_desc))

            return Responses(result=responses)

        except Exception as e:
            logger.error(e)
            raise
