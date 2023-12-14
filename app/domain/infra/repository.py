from abc import ABC, abstractmethod
from pathlib import Path

from pandera.typing import DataFrame

from app.domain.schema import DescBySignSchema


class IDescBySignRepository(ABC):
    @abstractmethod
    def read_csv(self, path: Path) -> DataFrame[DescBySignSchema]:
        """
        Abstract method to read a CSV file and return a Pandas DataFrame with DescBySignSchema.

        Parameters
        ----------
        path : Path
            The path to the CSV file.

        Returns
        -------
        DataFrame[DescBySignSchema]
            Pandas DataFrame with DescBySignSchema.
        """
        raise NotImplementedError
