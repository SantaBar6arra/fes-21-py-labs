from cell import Cell
from math import sqrt
import random

class EmployedBee(object):
    __foodCapacity: int
    __foodGathered: int
    __currentPosition: Cell
    
    def __init__(self, capacity: int):
        self.__foodCapacity = capacity
        self.__foodGathered = 0


    def fly(self, src: Cell):
        self.__currentPosition = src

        if self.__currentPosition.currentLoad >= self.__currentPosition.max_load:
            self.__currentPosition.currentLoad += 1
            raise ValueError('Overloaded')
        
        if self.__currentPosition.value == 0:
            self.__currentPosition.currentLoad += 1
            raise ValueError('No honey, i\'m going home')

        self.__currentPosition.currentLoad += 1


    def gather(self):
        available_storage: int = self.__foodCapacity - self.__foodGathered
        print(f'Avalilable storage: {available_storage}, '
              + f'Trying to gather value from cell ({self.__currentPosition.x}; ' 
              + f'{self.__currentPosition.y}) with value {self.__currentPosition.value}')

        if self.__currentPosition.value <= available_storage:
            print('Bee can gather it all')
            self.__foodGathered += self.__currentPosition.value
            self.__currentPosition.value = 0
        else:
            print('Bee cann\'t gather it all')
            self.__foodGathered += available_storage
            self.__currentPosition.value -= available_storage

        
    def returnGatheredFood(self) -> int:
        self.__currentPosition.currentLoad -= 1
        foodGathered = self.__foodGathered
        self.__foodGathered = 0
        return foodGathered
    

class InspectorBee:
    def check_src_quality(self, food_gathered: int, src: Cell) -> float:        
        distance: float = sqrt(src.x**2 + src.y**2)

        return random.random() * food_gathered / distance
