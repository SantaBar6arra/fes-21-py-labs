class Cell:
    __pos_x: int
    __pos_y: int
    __max_load: int
    cur_load: int
    val: int
    
    def __init__(self, pos_x: int, pos_y: int, max_load: int) -> None:
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__max_load = max_load
        self.cur_load = 0
        self.val = 0
        
    @property
    def x(self) -> int:
        return self.__pos_x
    
    @property
    def y(self) -> int:
        return self.__pos_y

    @property
    def max_load(self) -> int:
        return self.__max_load