from abc import ABC, abstractmethod
from pathlib import Path

from pandera.typing import DataFrame

from app.domain.schema import DescBySignSchema


class IDescBySignRepository(ABC):
    def __init__(self, path: Path) -> None:
        raise NotImplementedError

    @abstractmethod
    def load(self) -> DataFrame[DescBySignSchema]:
        raise NotImplementedError
