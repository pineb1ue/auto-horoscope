from pathlib import Path

from dependency_injector import containers, providers

from app.infra.repository import DescBySignRepository
from app.usecase.fetch_desc_usecase import FetchDescUsecase
from app.usecase.horoscope_usecase import HoroscopeUsecase
from app.usecase.house_usecase import HouseUsecase


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["app.presentation.router"])

    config = providers.Configuration(yaml_files=["config.yml"])
    config.load()

    desc_by_sign_repo = providers.Factory(DescBySignRepository, path=Path(config()["desc_path"]))
    fetch_desc_usecase = providers.Factory(FetchDescUsecase, desc_by_sign_repo=desc_by_sign_repo)

    house_usecase = providers.Factory(HouseUsecase)
    horoscope_usecase = providers.Factory(HoroscopeUsecase, house_usecase=house_usecase)
