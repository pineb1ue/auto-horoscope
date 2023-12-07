from datetime import datetime

from pytz import timezone


class TimezoneUsecase:
    def convert_to_utc_from_jst(
        self,
        yyyy: int,
        mm: int,
        dd: int,
        HH: int,
        MM: int,
    ) -> datetime:
        dt = datetime(yyyy, mm, dd, HH, MM, 0)
        dt_jst = dt.astimezone(timezone("Asia/Tokyo"))
        dt_utc = dt_jst.astimezone(timezone("UTC"))
        return dt_utc
