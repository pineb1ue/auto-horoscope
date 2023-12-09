from injector import Binder, Module, provider

from app.domain.infra.repository import IDescBySignRepository
from app.infra.repository import DescBySignRepository


class AstrologyModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(IDescBySignRepository, to=DescBySignRepository)  # type: ignore[type-abstract]

    @provider
    def provide_desc_by_repository(self, repo: IDescBySignRepository) -> IDescBySignRepository:
        return repo
