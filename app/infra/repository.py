from pathlib import Path
from typing import cast

import pandas as pd
from domain.infra.repository import IDescBySignRepository
from domain.res import DescBySignSchema
from exception import CsvFileNotFoundError
from loguru import logger
from pandera.typing import DataFrame


class DescBySignRepository(IDescBySignRepository):
    def read_csv(self, path: Path) -> DataFrame[DescBySignSchema]:
        try:
            return cast(DataFrame[DescBySignSchema], pd.read_csv(path))
        except FileNotFoundError as e:
            logger.error(e)
            raise CsvFileNotFoundError(e)
