from pathlib import Path
from typing import cast

import pandas as pd
from loguru import logger
from pandera.typing import DataFrame

from app.domain.infra.repository import IDescBySignRepository
from app.domain.schema import DescBySignSchema
from app.exceptions.exception import CsvFileNotFoundError


class DescBySignRepository(IDescBySignRepository):
    def __init__(self, path: Path) -> None:
        self.path = path

    def load(self) -> DataFrame[DescBySignSchema]:
        try:
            logger.info("Start DescBySignRepository")
            df = pd.read_csv(self.path)
            logger.info("End DescBySignRepository")
            return cast(DataFrame[DescBySignSchema], df)
        except FileNotFoundError as e:
            logger.error(e)
            raise CsvFileNotFoundError()
