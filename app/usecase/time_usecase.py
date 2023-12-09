from datetime import datetime
from typing import cast

import swisseph as swe
from pytz import timezone


class TimeUsecase:
    @classmethod
    def convert_to_julian_day(cls, yyyy: int, mm: int, dd: int, HH: int, MM: int) -> datetime:
        dt = datetime(yyyy, mm, dd, HH, MM, 0)
        dt_jst = dt.astimezone(timezone("Asia/Tokyo"))
        dt_utc = dt_jst.astimezone(timezone("UTC"))
        return cast(
            datetime,
            swe.julday(
                dt_utc.year,
                dt_utc.month,
                dt_utc.day,
                dt_utc.hour + dt_utc.minute / 60 + dt_utc.second / 3600,
            ),
        )
