import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import swisseph as swe
from pytz import timezone


def plot_polar_coordinates(planet_names: list[str], planet_longitudes: list[float]):
    fig, ax = plt.subplots(subplot_kw={"projection": "polar"}, figsize=(8, 8))

    for name, longitude in zip(planet_names, planet_longitudes):
        radian_angle = np.radians(longitude)
        ax.plot(radian_angle, 1, "o", label=name)

    ax.set_rmax(1.2)
    ax.set_rgrids([])
    ax.set_thetagrids(range(0, 360, 30))
    ax.set_title("Horoscope")

    ax.legend()
    plt.show()


def calculate_planet_position(dt: datetime.datetime, lat: float, lon: float, planet_id: int) -> list[float]:
    jd_utc = swe.julday(dt.year, dt.month, dt.day, dt.hour + dt.minute / 60.0 + dt.second / 3600.0)
    flag = swe.FLG_SWIEPH | swe.FLG_SPEED
    swe.set_topo(lat, lon, 0.0)
    topocentric_position, _ = swe.calc_ut(jd_utc, planet_id, flag | swe.FLG_TOPOCTR)
    return topocentric_position


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def input_your_birth_and_location(
    yyyy: int,
    mm: int,
    dd: int,
    HH: int,
    MM: int,
    latitude: float = 36.4000,
    longitude: float = 139.4600,
) -> tuple[datetime.datetime, float, float]:
    input_datetime = datetime.datetime(yyyy, mm, dd, HH, MM, 0)
    input_datetime_jst = input_datetime.astimezone(timezone("Asia/Tokyo"))
    input_datetime_utc = input_datetime_jst.astimezone(timezone("UTC"))
    return input_datetime_utc, latitude, longitude


def main():
    df = load_data("data/desc_sign.csv")
    your_birth, input_latitude, input_longitude = input_your_birth_and_location(1997, 12, 30, 23, 20)

    planet_dict = {
        "太陽": swe.SUN,
        "月": swe.MOON,
        "水星": swe.MERCURY,
        "金星": swe.VENUS,
        "火星": swe.MARS,
        "木星": swe.JUPITER,
        "土星": swe.SATURN,
    }
    sign_dict = {
        i: sign
        for i, sign in enumerate(
            [
                "牡羊",
                "牡牛",
                "双子",
                "蟹",
                "獅子",
                "乙女",
                "天秤",
                "蠍",
                "射手",
                "山羊",
                "水瓶",
                "魚",
            ]
        )
    }

    your_signs = []
    planet_longitudes = []

    for planet_name, planet_id in planet_dict.items():
        topocentric_position = calculate_planet_position(your_birth, input_latitude, input_longitude, planet_id)
        sign_id = int(topocentric_position[0] // 30)
        your_signs.append(sign_dict[sign_id])

        planet_longitudes.append(topocentric_position[0])

    for planet_name, your_sign in zip(planet_dict.keys(), your_signs):
        print(df[(df["惑星"] == planet_name) & (df["星座"] == your_sign)].values)

    plot_polar_coordinates(list(planet_dict.keys()), planet_longitudes)


if __name__ == "__main__":
    main()
