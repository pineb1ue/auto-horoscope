from pathlib import Path

from dependency_injector import containers, providers

from app.infra.repository import DescRepository
from app.usecase.desc_usecase import DescUsecase
from app.usecase.horoscope_usecase import HoroscopeUsecase
from app.usecase.house_usecase import HouseUsecase


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["app.presentation.endpoint"])

    config = providers.Configuration(yaml_files=["config.yml"])
    config.load()

    desc_repo = providers.Factory(DescRepository, path=Path(config()["desc_path"]))
    desc_usecase = providers.Factory(DescUsecase, desc_repo=desc_repo)

    house_usecase = providers.Factory(HouseUsecase)
    horoscope_usecase = providers.Factory(HoroscopeUsecase, house_usecase=house_usecase)
