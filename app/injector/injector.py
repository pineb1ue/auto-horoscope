from injector import Binder, Injector, inject

from app.injector.module import AstrologyModule


@inject
def configure(binder: Binder) -> None:
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
    binder.install(AstrologyModule())


injector = Injector([AstrologyModule])
