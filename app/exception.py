class CsvFileNotFoundError(Exception):
    def __init__(self) -> None:
        super().__init__("Not found csv file.")


class TopocentricCalculationError(Exception):
    def __init__(self) -> None:
        super().__init__("Error during topocentric position calculation.")
