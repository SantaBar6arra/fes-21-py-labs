class Cell:
    __positionX: int
    __positionY: int
    __maxLoad: int
    currentLoad: int
    value: int
    
    def __init__(self, positionX: int, positionY: int, maxLoad: int) -> None:
        self.__positionX = positionX
        self.__positionY = positionY
        self.__maxLoad = maxLoad
        self.currentLoad = 0
        self.value = 0
        
    @property
    def x(self) -> int:
        return self.__positionX
    
    @property
    def y(self) -> int:
        return self.__positionY

    @property
    def max_load(self) -> int:
        return self.__maxLoad