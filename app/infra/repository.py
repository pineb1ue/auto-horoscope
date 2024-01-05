from pathlib import Path
from typing import cast

import pandas as pd
from loguru import logger
from pandera.typing import DataFrame

from app.domain.exception import CsvFileNotFoundError
from app.domain.infra.repository import IDescRepository
from app.domain.schema import DescSchema


class DescRepository(IDescRepository):
    def __init__(self, path: Path) -> None:
        self.path = path

    def get_all(self) -> DataFrame[DescSchema]:
        try:
            logger.info("Start DescRepository")
            df = pd.read_csv(self.path)
            logger.info("End DescRepository")
            return cast(DataFrame[DescSchema], df)
        except FileNotFoundError as e:
            logger.error(e)
            raise CsvFileNotFoundError()
