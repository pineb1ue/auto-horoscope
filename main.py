import pandas as pd

from app.domain.io import Request
from app.presentation.controller import AstrologyController

if __name__ == "__main__":
    req = {
        "yyyy": 1997,
        "mm": 11,
        "dd": 3,
        "HH": 5,
        "MM": 58,
    }
    controller = AstrologyController(Request(**req))
    controller.get_desc_by_sign(df=pd.read_csv("data/desc_sign.csv"))
