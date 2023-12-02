import datetime

import matplotlib.pyplot as plt
import numpy as np
import swisseph as swe
from pytz import timezone


def plot_polar_coordinates(planet_names, planet_longitudes):
    # 描画の準備
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 8))

    # 各惑星の座標を極座標系でプロット
    for name, longitude in zip(planet_names, planet_longitudes):
        radian_angle = np.radians(longitude)
        ax.plot(radian_angle, 1, 'o', label=name)

    # グラフを整える
    ax.set_rmax(1.2)  # 半径の最大値
    ax.set_rgrids([])
    ax.set_thetagrids(range(0, 360, 30))
    ax.set_title("Horoscope")

    # 凡例を表示
    ax.legend()

    # 描画を表示
    plt.show()


def calculate_planet_position(date_time, latitude, longitude, planet_id):
    jd_utc = swe.julday(date_time.year, date_time.month, date_time.day,
                        date_time.hour + date_time.minute / 60.0 + date_time.second / 3600.0)

    flag = swe.FLG_SWIEPH | swe.FLG_SPEED

    swe.set_topo(latitude, longitude, 0.0)

    planet_position, _ = swe.calc_ut(jd_utc, planet_id, flag)
    topocentric_position, _ = swe.calc_ut(jd_utc, planet_id, flag | swe.FLG_TOPOCTR)

    return planet_position, topocentric_position


def main():
    input_date_time = datetime.datetime(1997, 12, 30, 23, 20, 0)
    input_date_time_jst = input_date_time.astimezone(timezone('Asia/Tokyo'))
    input_date_time_utc = input_date_time_jst.astimezone(timezone('UTC'))

    input_latitude = 36.4000  # Example latitude (Tokyo)
    input_longitude = 139.4600  # Example longitude (Tokyo)

    planet_dict = {
        "Sun": swe.SUN,
        "Moon": swe.MOON,
        "Mercury": swe.MERCURY,
        "Venus": swe.VENUS,
        "Mars": swe.MARS,
        "Jupiter": swe.JUPITER,
        "Saturn": swe.SATURN,
        "Uranus": swe.URANUS,
        "Neptune": swe.NEPTUNE,
        "Pluto": swe.PLUTO,
    }

    planet_longitudes = []

    for planet_id in planet_dict.values():
        _, topocentric_position = calculate_planet_position(
            input_date_time_utc, input_latitude, input_longitude, planet_id)

        # Print results
        print(f"黄経（Ecliptic Longitude）: {topocentric_position[0]}")
        planet_longitudes.append(topocentric_position[0])

    plot_polar_coordinates(list(planet_dict.keys()), planet_longitudes)


if __name__ == "__main__":
    main()
