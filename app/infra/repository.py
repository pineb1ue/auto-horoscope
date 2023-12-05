from pathlib import Path
from typing import cast

import pandas as pd
from loguru import logger
from pandera.typing import DataFrame

from app.domain.infra.repository import IDescBySignRepository
from app.domain.schema import DescBySignSchema
from app.exception import CsvFileNotFoundError


class DescBySignRepository(IDescBySignRepository):
    def read_csv(self, path: Path) -> DataFrame[DescBySignSchema]:
        try:
            return cast(DataFrame[DescBySignSchema], pd.read_csv(path))
        except FileNotFoundError as e:
            logger.error(e)
            raise CsvFileNotFoundError(e)
