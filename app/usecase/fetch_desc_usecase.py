from loguru import logger

from app.domain.horoscope import HoroDesc
from app.domain.infra.repository import IDescBySignRepository
from app.domain.planet import Planet
from app.usecase.sign_usecase import SignUsecase


class FetchDescUsecase:
    def __init__(self, desc_by_sign_repo: IDescBySignRepository) -> None:
        self.desc_by_sign_repo = desc_by_sign_repo

    def run(self, jd_utc: float, lat: float = 36.4000, lon: float = 139.4600) -> list[HoroDesc]:
        try:
            logger.info("Start FetchDescUsecase")

            # Calculate the positions of planets
            planet_positions = Planet.calc_planet_positions(jd_utc, lat, lon)

            your_signs = SignUsecase.assign_signs_to_planets(planet_positions)
            your_descriptions = self._fetch_horoscope_descriptions(your_signs)

            responses = []
            for planet, your_sign, your_desc in zip(Planet, your_signs, your_descriptions):
                responses.append(HoroDesc(planet_id=planet.value, sign_id=your_sign, description=your_desc))

            logger.info("End FetchDescUsecase")

            return responses

        except Exception as e:
            logger.error(e)
            raise

    def _fetch_horoscope_descriptions(self, signs: list[int]) -> list[str]:
        """
        Fetch horoscope descriptions based on astrological signs.

        Parameters
        ----------
        signs : list[int]
            A list of astrological signs for which descriptions will be fetched.

        Returns
        -------
        list[str]
            A list of horoscope descriptions corresponding to the provided signs.
        """
        df = self.desc_by_sign_repo.load()

        desc_by_signs = []
        for planet, sign in zip(Planet, signs):
            desc_by_sign = df[(df["planet_id"] == planet.value) & (df["sign_id"] == sign)].loc[:, "desc"].values[0]
            desc_by_signs.append(desc_by_sign)

        return desc_by_signs
