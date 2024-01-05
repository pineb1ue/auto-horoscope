from abc import ABC, abstractmethod
from pathlib import Path

from pandera.typing import DataFrame

from app.domain.schema import DescSchema


class IDescRepository(ABC):
    def __init__(self, path: Path) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> DataFrame[DescSchema]:
        raise NotImplementedError
