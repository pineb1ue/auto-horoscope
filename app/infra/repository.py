from pathlib import Path
from typing import cast

import pandas as pd
from pandera.typing import DataFrame

from app.domain.infra.repository import IDescBySignRepository
from app.domain.res import DescBySignSchema


class DescBySignRepository(IDescBySignRepository):
    def read_csv(self, path: Path) -> DataFrame[DescBySignSchema]:
        return cast(DataFrame[DescBySignSchema], pd.read_csv(path))
