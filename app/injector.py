from injector import Binder, Injector, Module

from app.domain.infra.repository import IDescBySignRepository
from app.infra.repository import DescBySignRepository
from app.presentation.controller import AstrologyController
from app.usecase.usecase import FetchDescUsecase


class AstrologyModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(AstrologyController)
        binder.bind(FetchDescUsecase)
        binder.bind(IDescBySignRepository, to=DescBySignRepository)  # type: ignore


injector = Injector([AstrologyModule])
