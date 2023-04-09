from math import sqrt
import random
from cell import Cell


class InspectorBee:
    def check_src_quality(self, food_gathered: int, src: Cell) -> float:        
        distance: float = sqrt(src.x**2 + src.y**2)

        return random.random() * food_gathered / distance
