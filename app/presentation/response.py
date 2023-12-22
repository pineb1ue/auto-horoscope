from pydantic import BaseModel


class Response(BaseModel):
    planet_id: int
    sign_id: int
    description: str
