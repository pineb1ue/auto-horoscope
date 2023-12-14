from pathlib import Path

from injector import inject

from app.domain.infra.repository import IDescBySignRepository
from app.domain.planet import Planet


class FetchDescUsecase:
    @inject
    def __init__(self, repo: IDescBySignRepository) -> None:
        """
        Initialize the FetchDescUsecase with the specified repository.

        Parameters
        ----------
        repo : IDescBySignRepository
            The repository for fetching horoscope descriptions.
        """
        self.repo = repo

    def fetch_horoscope_descriptions(self, signs: list[int], path: Path) -> list[str]:
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
        df = self.repo.read_csv(path)

        desc_by_signs = []
        for planet, sign in zip(Planet, signs):
            desc_by_sign = df[(df["planet_id"] == planet.value) & (df["sign_id"] == sign)].loc[:, "desc"].values[0]
            desc_by_signs.append(desc_by_sign)

        return desc_by_signs
