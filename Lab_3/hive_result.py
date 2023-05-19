from pydantic import BaseModel
from cell_dto import CellDto


class HiveIterationResultPerBee(BaseModel):
    bee_no: int or None = 0
    available_storage: int or None = 0
    cell: CellDto or None = 0
    verdict: str or None = 0
