from pydantic import BaseModel


class CellDto(BaseModel):
    x: int = 0
    y: int = 0
    val: int = 0
    max_load: int = 0
