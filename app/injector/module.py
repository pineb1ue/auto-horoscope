from injector import Binder, Module, provider

from app.domain.infra.repository import IDescBySignRepository
from app.infra.repository import DescBySignRepository


class AstrologyModule(Module):
    def configure(self, binder: Binder) -> None:
        """
        Configures dependency injection bindings.

        Parameters
        ----------
        binder : Binder
            The binder to configure.

        Returns
        -------
        None
        """
        binder.bind(IDescBySignRepository, to=DescBySignRepository)  # type: ignore[type-abstract]

    @provider
    def provide_desc_by_repository(self, repo: IDescBySignRepository) -> IDescBySignRepository:
        """
        Provides the implementation of the IDescBySignRepository interface.

        Parameters
        ----------
        repo : IDescBySignRepository
            The repository instance.

        Returns
        -------
        IDescBySignRepository
            The provided repository instance.
        """
        return repo
