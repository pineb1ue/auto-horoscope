from abc import ABC, abstractmethod
from pathlib import Path

from pandera.typing import DataFrame

from app.domain.res import DescBySignSchema


class IDescBySignRepository(ABC):
    @abstractmethod
    def read_csv(self, path: Path) -> DataFrame[DescBySignSchema]:
        raise NotImplementedError
