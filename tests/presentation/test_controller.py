import itertools
from pathlib import Path

import pandas as pd
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from loguru import logger

from app.domain.io import Request, Response, Responses
from app.domain.planet import Planet
from app.domain.sign import Sign
from app.presentation.controller import AstrologyController
from app.usecase.astrology_usecase import AstrologyUsecase


def test_fetch_horoscope_descriptions(mocker, tmpdir):
    # tmpfile = tmpdir.join("desc_sign.csv")
    # df = pd.DataFrame(
    #     {
    #         "planet_id": list(
    #             itertools.chain.from_iterable(
    #                 [[i] * len(Sign) for i in range(len(Planet))],
    #             ),
    #         ),
    #         "sign_id": list(
    #             itertools.chain.from_iterable(
    #                 [[i for i in range(len(Sign))] for j in range(len(Planet))],
    #             )
    #         ),
    #         "desc": [f"desc{i}" for i in range(len(Sign) * len(Planet))],
    #     }
    # )
    # df.to_csv(tmpfile)

    mocked_req = mocker.Mock(spce=Request)
    mocked_path = mocker.Mock(spce=Path)
    mocked_astrology_usecase = mocker.Mock(spec=AstrologyUsecase)

    mocked_req.convert_to_julian_day.return_value = 2450813.472222222
    mocker.patch("app.usecase.astrology_usecase.AstrologyUsecase", return_value=mocked_astrology_usecase)
    mocked_astrology_usecase.assign_signs_to_planets.return_value = [0, 1, 2, 3, 4, 5, 6]
    mocked_astrology_usecase.fetch_horoscope_descriptions.return_value = [
        "desc0",
        "desc1",
        "desc2",
        "desc3",
        "desc4",
        "desc5",
        "desc6",
    ]

    # actual
    controller = AstrologyController()
    actual = controller.fetch_horoscope_descriptions(mocked_req, mocked_path, latitude=36.4000, longitude=139.4600)

    # expected
    expected = JSONResponse(
        content=jsonable_encoder(
            Responses(
                result=[
                    Response(planet_id=Planet.SUN.value, sign_id=0, description="desc0"),
                    Response(planet_id=Planet.MOON.value, sign_id=1, description="desc1"),
                    Response(planet_id=Planet.MERCURY.value, sign_id=2, description="desc2"),
                    Response(planet_id=Planet.VENUS.value, sign_id=3, description="desc3"),
                    Response(planet_id=Planet.MARS.value, sign_id=4, description="desc4"),
                    Response(planet_id=Planet.JUPITER.value, sign_id=5, description="desc5"),
                    Response(planet_id=Planet.SATURN.value, sign_id=6, description="desc6"),
                ]
            )
        )
    )

    logger.info(actual.body)

    # assert
    assert isinstance(actual, JSONResponse)
    # assert actual == expected

    # tmpfile.remove()
