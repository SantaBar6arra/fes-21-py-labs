from pydantic import BaseModel

class Config(BaseModel):
    field_height: int = 20   
    field_width: int = 20   
    field_capacity: int = 100
    colony_size: int = 5
    employed: int = 3
    sources: int = 10
    DIMENSION: int = 2
