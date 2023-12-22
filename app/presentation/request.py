from datetime import datetime

import swisseph as swe
from pydantic import BaseModel
from pytz import timezone


class Request(BaseModel):
    yyyy: int
    mm: int
    dd: int
    HH: int
    MM: int
    latitude: float = 36.4000
    longitude: float = 139.4600

    def convert_to_julian_day(self) -> float:
        """
        Converts the request date and time to Julian day.

        Returns
        -------
        float
            The converted Julian day.
        """
        dt = datetime(self.yyyy, self.mm, self.dd, self.HH, self.MM)
        dt_jst = dt.astimezone(timezone("Asia/Tokyo"))
        dt_utc = dt_jst.astimezone(timezone("UTC"))
        return float(
            swe.julday(
                dt_utc.year,
                dt_utc.month,
                dt_utc.day,
                dt_utc.hour + dt_utc.minute / 60 + dt_utc.second / 3600,
            )
        )
