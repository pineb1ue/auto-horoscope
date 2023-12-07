from pathlib import Path

from injector import inject

from app.domain.infra.repository import IDescBySignRepository
from app.domain.planet import Planet


class FetchDescUsecase:
    @inject
    def __init__(self, repo: IDescBySignRepository) -> None:
        self.repo = repo

    def fetch_desc_by_signs(self, path: Path, sings: list[int]) -> list[str]:
        df = self.repo.read_csv(path)

        desc_by_signs = []
        for planet, sign in zip(Planet, sings):
            desc_by_sign = df[(df["planet_id"] == planet.value) & (df["sign_id"] == sign)].loc[:, "desc"].values[0]
            desc_by_signs.append(desc_by_sign)

        return desc_by_signs
