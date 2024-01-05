import pandera as pa
from pandera.typing import Series


class DescSchema(pa.DataFrameModel):
    planet_id: Series[int]
    sign_id: Series[int]
    desc: Series[str]
