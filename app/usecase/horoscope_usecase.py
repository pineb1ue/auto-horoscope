from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from app.domain.planet import PlanetEmoji
from app.domain.sign import SignEmoji
from app.usecase.house_usecase import HouseUsecase


class HoroscopeUsecase:
    def __init__(self, jd_utc: float, lat: float, lon: float) -> None:
        """
        Initialize the HoroscopeUsecase with the specified parameters.

        Parameters
        ----------
        jd_utc : float
            The Julian date in UTC.
        lat : float
            The latitude of the location.
        lon : float
            The longitude of the location.
        """
        self.jd_utc = jd_utc
        self.lat = lat
        self.lon = lon

    def create_and_save_horoscope(self, planet_positions: list[float], save_path: Path) -> None:
        """
        Create a horoscope and save it to the specified path.

        Parameters
        ----------
        planet_positions : list[float]
            The positions of the planets.
        save_path : Path
            The path where the horoscope will be saved.
        """
        # Calculate house positions and ascendant
        house_usecase = HouseUsecase(self.jd_utc, self.lat, self.lon)
        house_positions, ascendant = house_usecase.calc_house_positions_and_ascendant()

        # Draw the horoscope chart and save it
        self._draw_and_save_horoscope_chart(ascendant, planet_positions, house_positions, save_path=save_path)

    def _draw_and_save_horoscope_chart(
        self,
        ascendant: float,
        planet_positions: list[float],
        house_positions: tuple[float],
        save_path: Path,
        color1: str = "blue",
        color2: str = "purple",
    ) -> None:
        """
        Draw a horoscope chart and save it to the specified path.

        Parameters
        ----------
        ascendant : float
            The ascendant angle.
        planet_positions : list[float]
            The positions of the planets.
        house_positions : tuple[float]
            The positions of the houses.
        save_path : Path
            The path where the horoscope chart will be saved.
        color1 : str
            The color for even signs in the pie chart.
        color2 : str
            The color for odd signs in the pie chart.
        """
        fig = plt.figure(figsize=(16, 12))
        ax1 = fig.add_axes((0, 0, 1, 1))

        ax1.pie(
            np.full(12, 30),
            labels=SignEmoji.get_values(),
            colors=[color1 if i % 2 == 0 else color2 for i in range(len(SignEmoji))],
            startangle=180 - ascendant,
        )
        ax1.axis("equal")

        # Add a polar subplot
        ax2 = fig.add_axes((0.15, 0.15, 0.7, 0.7), projection="polar")

        # Plot the planets on the polar graph
        for planet_position, planet_emoji in zip(planet_positions, PlanetEmoji.get_values()):
            ax2.scatter(
                np.radians(planet_position),
                np.ones_like(planet_position),
                s=80,
                marker=planet_emoji,
            )

        ax2.set_xticks(np.radians(house_positions))
        ax2.set_rgrids([0.8, 1.1])  # type: ignore[attr-defined]

        ax2.set_xticklabels([])
        ax2.set_yticklabels([])

        ax2.axes.xaxis.set_ticklabels([])  # type: ignore[union-attr]
        ax2.axes.yaxis.set_ticklabels([])  # type: ignore[union-attr]
        ax2.grid(True)

        ax2.set_theta_zero_location("E", offset=180 - ascendant)  # type: ignore[attr-defined]

        fig.savefig(str(save_path))
