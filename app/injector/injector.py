from injector import Binder, Injector, inject

from app.injector.module import AstrologyModule


@inject
def configure(binder: Binder) -> None:
    binder.install(AstrologyModule())


injector = Injector([AstrologyModule])
