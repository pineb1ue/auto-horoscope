from pydantic import BaseModel


class Request(BaseModel):
    yyyy: int
    mm: int
    dd: int
    HH: int
    MM: int
    latitude: float = 36.4000
    longitude: float = 139.4600


class Response(BaseModel):
    planet_id: int
    sign_id: int
    description: str


class Responses(BaseModel):
    result: list[Response]
