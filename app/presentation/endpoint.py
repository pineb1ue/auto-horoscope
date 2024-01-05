from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.domain.container import Container
from app.domain.horoscope import HoroDesc
from app.presentation.request import Request
from app.usecase.desc_usecase import DescUsecase
from app.usecase.horoscope_usecase import HoroscopeUsecase

router = APIRouter()


@router.post("/api/v1/horo/desc")
@inject
async def get_horoscope_descriptions(
    req: Request,
    desc_usecase: DescUsecase = Depends(Provide[Container.desc_usecase]),
) -> list[HoroDesc]:
    return desc_usecase.get_desc(req.convert_to_julian_day(), req.latitude, req.longitude)


@router.post("/api/v1/horo/fig")
async def create_horoscope_figure(
    req: Request,
    horoscope_usecase: HoroscopeUsecase = Depends(Provide[Container.horoscope_usecase]),
) -> JSONResponse:
    horoscope_usecase.create(req.convert_to_julian_day(), req.latitude, req.longitude)

    return JSONResponse(content=None, status_code=200)
