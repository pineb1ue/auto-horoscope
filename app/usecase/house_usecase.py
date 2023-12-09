from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import swisseph as swe

from app.domain.planet import PlanetEmoji
from app.domain.sign import SignEmoji


class HouseUsecase:
    def __init__(self, jd_utc: datetime, lat: float, lon: float) -> None:
        self.jd_utc = jd_utc
        self.lat = lat
        self.lon = lon

    def calc_house_and_ascendant(self) -> tuple[tuple[float], float]:
        swe.set_ephe_path("/Users/pineb1ue/Desktop/ast1")  # ephemerisファイルへのパスを指定
        house_positions, asmc = swe.houses(self.jd_utc, self.lat, self.lon)
        ascendant = asmc[0]
        return house_positions, ascendant

    def draw_horoscope_chart(
        self,
        ascendant: float,
        planet_positions: list[float],
        house_positions: tuple[float],
        save_path: Path = Path("/Users/pineb1ue/Desktop/sample.png"),
        color1: str = "blue",
        color2: str = "purple",
    ) -> None:
        fig = plt.figure(figsize=(16, 12))
        ax1 = fig.add_axes((0, 0, 1, 1))

        ax1.pie(
            np.full(12, 30),
            labels=SignEmoji.get_values(),
            colors=[color1 if i % 2 == 0 else color2 for i in range(len(SignEmoji))],
            startangle=180 - ascendant,
        )
        ax1.axis("equal")

        # 極座標サブプロットを追加
        ax2 = fig.add_axes((0.15, 0.15, 0.7, 0.7), projection="polar")

        # グラフを描画
        for planet_position, planet_emoji in zip(planet_positions, PlanetEmoji.get_values()):
            ax2.scatter(
                np.radians(planet_position),
                np.ones_like(planet_position),
                s=80,
                marker=planet_emoji,
            )

        ax2.set_xticks(np.radians(house_positions))
        ax2.set_rgrids([0.8, 1.1])  # type: ignore

        ax2.set_xticklabels([])
        ax2.set_yticklabels([])

        ax2.axes.xaxis.set_ticklabels([])  # type: ignore
        ax2.axes.yaxis.set_ticklabels([])  # type: ignore
        ax2.grid(True)

        ax2.set_theta_zero_location("E", offset=180 - ascendant)  # type: ignore

        fig.savefig(str(save_path))
