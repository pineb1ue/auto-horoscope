from pydantic import BaseModel


class HoroDesc(BaseModel):
    planet_id: int
    sign_id: int
    description: str
