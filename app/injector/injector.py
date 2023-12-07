from injector import Injector  # type: ignore

from app.injector.module import AstrologyModule

injector = Injector([AstrologyModule])
