class CsvFileNotFoundError(Exception):
    def __init__(self) -> None:
        """
        Exception for indicating that the CSV file is not found.
        """
        super().__init__("Not found csv file.")


class TopocentricCalculationError(Exception):
    def __init__(self) -> None:
        """
        Exception for indicating an error during topocentric position calculation.
        """
        super().__init__("Error during topocentric position calculation.")
