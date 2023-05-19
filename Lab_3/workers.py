from hive import Cell
from math import sqrt
import random


class EmployedBee(object):
    __food_capacity: int
    __food_gathered: int
    __cur_pos: Cell
    
    def __init__(self, capacity: int):
        self.__food_capacity = capacity
        self.__food_gathered = 0


    def fly(self, src: Cell):
        self.__cur_pos = src

        if self.__cur_pos.cur_load >= self.__cur_pos.max_load:
            self.__cur_pos.cur_load += 1
            raise ValueError('resource overloaded')
        
        if self.__cur_pos.val == 0:
            self.__cur_pos.cur_load += 1
            raise ValueError('no honey, no money, i go home')

        self.__cur_pos.cur_load += 1


    def gather(self):
        # should be only called after fly(src)
        available_storage: int = self.__food_capacity - self.__food_gathered

        if self.__cur_pos.val <= available_storage:
            self.__food_gathered += self.__cur_pos.val
            self.__cur_pos.val = 0
        else:
            self.__food_gathered += available_storage
            self.__cur_pos.val -= available_storage
            raise ValueError('bee CANNOT gather it all')

        
    def upload_food(self) -> int:
        # return food gathered
        self.__cur_pos.cur_load -= 1
        food_gathered = self.__food_gathered
        self.__food_gathered = 0
        return food_gathered

    @property
    def capacity(self) -> int:
        return self.__food_capacity

class InspectorBee:
    def check_src_quality(self, food_gathered: int, src: Cell) -> float:        
        distance: float = sqrt(src.x**2 + src.y**2)

        return random.random() * food_gathered / distance
