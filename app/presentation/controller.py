from pathlib import Path

from loguru import logger

from app.domain.io import Request, Response, Responses
from app.domain.planet import Planet
from app.usecase.astrology_usecase import AstrologyUsecase


class AstrologyController:
    def __init__(self) -> None:
        pass

    def fetch_desc_by_signs(
        self,
        req: Request,
        path: Path,
        latitude: float = 36.4000,
        longitude: float = 139.4600,
    ) -> Responses:
        try:
            jd_utc = req.convert_to_julian_day()

            astrology_usecase = AstrologyUsecase(jd_utc, latitude, longitude)

            # ホロスコープ作成
            astrology_usecase.create_horoscope(save_path=Path("/Users/pineb1ue/Desktop/sample.png"))
            # サインの計算
            your_signs = astrology_usecase.assign_sign_to_planets()
            # 文章作成
            your_descriptions = astrology_usecase.fetch_desc_by_signs(your_signs, path)

            responses = []
            for planet, your_sign, your_desc in zip(Planet, your_signs, your_descriptions):
                responses.append(Response(planet_id=planet.value, sign_id=your_sign, description=your_desc))

            return Responses(result=responses)

        except Exception as e:
            logger.error(e)
            raise
