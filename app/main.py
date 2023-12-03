from pathlib import Path

from domain.infra.repository import IDescBySignRepository
from domain.io import Request
from infra.repository import DescBySignRepository
from injector import Binder, Injector, Module
from presentation.controller import AstrologyController
from usecase.usecase import FetchDescUsecase


def main(controller: AstrologyController) -> None:
    req = {
        "yyyy": 1997,
        "mm": 11,
        "dd": 3,
        "HH": 5,
        "MM": 58,
    }
    controller.fetch_desc_by_signs(Request(**req), Path("data/desc_sign.csv"))


class AstrologyModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(AstrologyController)
        binder.bind(FetchDescUsecase)
        binder.bind(IDescBySignRepository, to=DescBySignRepository)  # type: ignore


if __name__ == "__main__":
    injector = Injector([AstrologyModule])
    main(injector.get(AstrologyController))
