from datetime import datetime
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import swisseph as swe


class HouseUsecase:
    def __init__(self, dt: datetime, lat: float, lon: float) -> None:
        self.dt = dt
        self.lat = lat
        self.lon = lon

    def calc_house_and_ascendant(self) -> tuple[tuple[float], float]:
        # Swiss Ephemerisの初期化
        swe.set_ephe_path("/Users/pineb1ue/Desktop/ast1")  # ephemerisファイルへのパスを指定
        # 出生時のユリウス日を計算
        jd_birth = self._calc_julian_day(self.dt)
        house_positions, asmc = swe.houses(jd_birth, self.lat, self.lon)
        ascendant = asmc[0]
        return house_positions, ascendant

    def draw_horoscope_chart(
        self,
        ascendant: float,
        planet_positions: list[float],
        house_positions: tuple[float],
        color1: str = "blue",
        color2: str = "purple",
        signs: list[str] = ["♈", "♉", "♊", "♋", "♌", "♍", "♎", "♏", "♐", "♑", "♒", "♓"],
        markers: list[str] = ["$☉$", "$☽$", "$☿$", "$♀$", "$♂$", "$♃$", "$♄$", "$♅$", "$♆$", "$♇$"],
    ) -> None:
        fig = plt.figure(figsize=(12, 12))
        ax1 = fig.add_axes((0, 0, 1, 1))

        values = np.full(12, 30)
        colors = [color1 if i % 2 == 0 else color2 for i in range(len(signs))]

        ax1.pie(values, labels=signs, colors=colors, startangle=180 - ascendant)
        ax1.axis("equal")

        # 極座標サブプロットを追加
        ax = fig.add_axes((0.15, 0.15, 0.7, 0.7), projection="polar")

        # グラフを描画
        for planet_position, marker in zip(planet_positions, markers):
            ax.scatter(
                np.radians(planet_position),
                np.ones_like(planet_position),
                s=80,
                marker=marker,
            )

        ax.set_xticks(np.radians(house_positions))
        ax.set_rgrids([0.8, 1.1])  # type: ignore

        ax.set_xticklabels([])
        ax.set_yticklabels([])

        ax.axes.xaxis.set_ticklabels([])  # type: ignore
        ax.axes.yaxis.set_ticklabels([])  # type: ignore
        ax.grid(True)

        ax.set_theta_zero_location("E", offset=180 - ascendant)  # type: ignore

        fig.savefig("/Users/pineb1ue/Desktop/sample.png")

    def _calc_julian_day(self, dt: datetime) -> Any:
        # 出生時のユリウス日を計算
        return swe.julday(
            dt.year,
            dt.month,
            dt.day,
            dt.hour + dt.minute / 60 + dt.second / 3600,
        )
