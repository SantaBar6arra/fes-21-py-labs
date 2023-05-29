import random
from cell_dto import CellDto
from workers import EmployedBee, InspectorBee
from hive_result import HiveIterationResultPerBee
from pydantic import BaseModel


class Config(BaseModel):
    field_height: int = 20   
    field_width: int = 20   
    field_capacity: int = 100
    colony_size: int = 5
    employed: int = 3
    sources: int = 10
    DIMENSION: int = 2

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
    

class FoodQuality:
    cell: Cell
    quality: float

    def __init__(self, cell: Cell, quality: float) -> None:
        self.cell = cell
        self.quality = quality


class BeeAssignment:
    bee: EmployedBee
    cell: Cell

    def __init__(self, bee: EmployedBee, cell: Cell) -> None:
        self.bee = bee
        self.cell = cell


class Hive: 
    __config: Config

    __food_gathered: float = 0
    __field: list[Cell]
    __picked_cells: list[Cell]
    __cells_quality_table: list[FoodQuality]
    __employed_bees: list[EmployedBee]
    __inspector_bee: InspectorBee
    
    
    def __init__(self, config: Config) -> None:
        self.__config = config
        
        self.__generate_field(self.__config.field_width, self.__config.field_height) 
        self.__generate_bees()
    
    
    def run(self) -> list[list[HiveIterationResultPerBee]]:
        hive_iterations_result: list[list[HiveIterationResultPerBee]] = []
        is_all_food_gathered: bool = False

        while is_all_food_gathered == False:
            bee_assignments: list[BeeAssignment] = self.__assign_bees_to_cells()
            hive_iteration_result: list[HiveIterationResultPerBee] = []

            for i in range(len(bee_assignments)):
                assignment: BeeAssignment = bee_assignments[i]

                if assignment.cell == None:
                    is_all_food_gathered = True
                    break

                hive_iteration_result.append(self.__generate_hive_iteration_result_per_bee(
                    i, assignment.cell, assignment.bee.capacity))

            if is_all_food_gathered:
                break

            for i in range(len(bee_assignments)):
                assignment: BeeAssignment = bee_assignments[i]

                try:
                    assignment.bee.fly(assignment.cell)
                    assignment.bee.gather()
                    hive_iteration_result[i].verdict = 'bee can gather it all'
                except ValueError as err:
                    hive_iteration_result[i].verdict = err.args[0]

            for i in range(len(bee_assignments)):
                assignment: BeeAssignment = bee_assignments[i]

                food_gathered_by_bee: int = assignment.bee.upload_food()
                self.__food_gathered += food_gathered_by_bee
 
                food_quality: float =  self.__inspector_bee.check_src_quality(food_gathered_by_bee, assignment.cell)
                self.__set_quality_to_cell(assignment.cell, food_quality)

            hive_iterations_result.append(hive_iteration_result)
        
        return hive_iterations_result

    
    def __generate_field(self, width: int, height: int) -> None:
        self.__field = [] 
        self.__cells_quality_table = []
    
        for h in range(height):
            for w in range(width):
                self.__field.append(Cell(w, h, random.randint(1, self.__config.employed)))
                
        self.__picked_cells: list = random.sample(self.__field, self.__config.sources)

        for i in range(len(self.__picked_cells)):
            field_cell: Cell = next((cell for cell in self.__field if cell.x == self.__picked_cells[i].x and cell.y == self.__picked_cells[i].y), None)
            field_cell.val = random.randint(0, self.__config.field_capacity)
            self.__cells_quality_table.append(FoodQuality(field_cell, float(0)))
    
            
    def __generate_bees(self) -> None:
        self.__employed_bees = []
        
        for i in range(self.__config.employed):
            self.__employed_bees.append(EmployedBee(random.randint(1, self.__config.field_capacity / 2)))

        self.__inspector_bee = InspectorBee()


    def __generate_hive_iteration_result_per_bee(self, bee_no: int, cell: Cell, available_storage: int):
        hive_iteration_result_per_bee = HiveIterationResultPerBee()
        hive_iteration_result_per_bee.bee_no = bee_no

        result_cell = CellDto()
        result_cell.x = cell.x
        result_cell.y = cell.y
        result_cell.val = cell.val
        result_cell.max_load = cell.max_load

        hive_iteration_result_per_bee.cell = result_cell
        hive_iteration_result_per_bee.available_storage = available_storage

        return hive_iteration_result_per_bee


    def __assign_bees_to_cells(self) -> list[BeeAssignment]:
        bee_assignments: list[BeeAssignment] = []

        for i in range(len(self.__employed_bees)):
            bee_assignments.append(BeeAssignment(self.__employed_bees[i],  self.__pick_cell_to_fly()))
        
        return bee_assignments


    def __set_quality_to_cell(self, cell: Cell, quality: float) -> None:
        for i in range(0, len(self.__cells_quality_table)):
            if self.__cells_quality_table[i].cell == cell:
                self.__cells_quality_table[i].quality = quality


    def __pick_cell_to_fly(self) -> Cell or None:
        sorted_quality_table = sorted(self.__cells_quality_table, key=lambda x: x.quality, reverse=True)

        for i in range(len(sorted_quality_table)):
            cell: Cell = sorted_quality_table[i].cell

            if cell.val == 0: 
                continue

            return cell
