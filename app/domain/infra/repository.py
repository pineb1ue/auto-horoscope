from abc import ABC, abstractmethod
from pathlib import Path

from domain.res import DescBySignSchema
from pandera.typing import DataFrame


class IDescBySignRepository(ABC):
    @abstractmethod
    def read_csv(self, path: Path) -> DataFrame[DescBySignSchema]:
        raise NotImplementedError
