from hive import Cell
from math import sqrt
import random


class Workerbee(object):
    __food_capacity: int
    __food_gathered: int
    __cur_pos: Cell
    
    def __init__(self, capacity: int):
        self.__food_capacity = capacity
        self.__food_gathered = 0


    def take_flight(self, src: Cell):
        self.__cur_pos = src

        if self.__cur_pos.cur_load >= self.__cur_pos.max_load:
            self.__cur_pos.cur_load += 1
            raise ValueError('Resource overloaded')
        
        if self.__cur_pos.val == 0:
            self.__cur_pos.cur_load += 1
            raise ValueError('No honey. I am coming home')

        self.__cur_pos.cur_load += 1


    def gather_honey(self):
        # should be only called after fly(src)
        available_storage: int = self.__food_capacity - self.__food_gathered
        print(f'Avalilable storage: {available_storage}, trying to gather value from cell ({self.__cur_pos.x}; {self.__cur_pos.y}) with value {self.__cur_pos.val}')

        if self.__cur_pos.val <= available_storage:
            print('Bee can gather it all')
            self.__food_gathered += self.__cur_pos.val
            self.__cur_pos.val = 0
        else:
            print('Bee cant gather it all')
            self.__food_gathered += available_storage
            self.__cur_pos.val -= available_storage

        
    def upload_food(self) -> int:
        # return food gathered
        self.__cur_pos.cur_load -= 1
        food_gathered = self.__food_gathered
        self.__food_gathered = 0
        return food_gathered

class QualityInspectorBee:
    def check_src_quality(self, food_gathered: int, src: Cell) -> float:        
        distance: float = sqrt(src.x**2 + src.y**2)

        return random.random() * food_gathered / distance
