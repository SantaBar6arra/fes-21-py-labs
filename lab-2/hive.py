import random
from cell import Cell
from constants import Constants
from bees import EmployedBee
from bees import InspectorBee


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
    __config: Constants

    __foodGathered: float = 0
    __field: list[Cell]
    __pickedCells: list[Cell]
    __cellsQualityTable: list[FoodQuality]
    __employedBees: list[EmployedBee]
    __inspectorBee: InspectorBee
    
    
    def __init__(self, config: Constants) -> None:
        self.__config = config
        
        self.__generateField(self.__config.FIELD_WIDTH, self.__config.FIELD_HEIGHT) 
        self.__generateBees()
    
    
    def run(self) -> None:        
        while True:
            beeAssignments: list[BeeAssignment] = self.__assignBeesToCells()

            for i in range(len(beeAssignments)):
                assignment: BeeAssignment = beeAssignments[i]

                if assignment.cell == None:
                    print('All the food gathered')
                    return

                print(f'Picked bee {i}')
                print(f'Picked cell ({assignment.cell.x}, {assignment.cell.y}) with value = {assignment.cell.value} and max load = {assignment.cell.max_load}')

            for i in range(len(beeAssignments)):
                assignment: BeeAssignment = beeAssignments[i]

                try:
                    assignment.bee.fly(assignment.cell)
                    assignment.bee.gather()
                except ValueError as err:
                    print(err)

            for i in range(len(beeAssignments)):
                assignment: BeeAssignment = beeAssignments[i]

                foodGatheredByBee: int = assignment.bee.returnGatheredFood()
                self.__foodGathered += foodGatheredByBee
 
                foodQuality: float =  self.__inspectorBee.check_src_quality(foodGatheredByBee, assignment.cell)
                print(f'Quality is {foodQuality}')
                self.__setQualityToCell(assignment.cell, foodQuality)   

    
    def __generateField(self, width: int, height: int) -> None:
        self.__field = [] 
        self.__cellsQualityTable = []
    
        for h in range(height):
            for w in range(width):
                self.__field.append(Cell(w, h, random.randint(1, self.__config.EMPLOYED_AGENTS)))
                
        self.__pickedCells: list = random.sample(self.__field, self.__config.SOURCES)

        for i in range(len(self.__pickedCells)):
            fieldCell: Cell = next((cell for cell in self.__field if cell.x == self.__pickedCells[i].x and cell.y == self.__pickedCells[i].y), None)
            fieldCell.value = random.randint(self.__config.MAX_FIELD_CAPACITY / 2, self.__config.MAX_FIELD_CAPACITY)
            self.__cellsQualityTable.append(FoodQuality(fieldCell, float(0)))
    
            
    def __generateBees(self) -> None:
        self.__employedBees = []
        
        for i in range(self.__config.EMPLOYED_AGENTS):
            self.__employedBees.append(EmployedBee(random.randint(1, self.__config.MAX_FIELD_CAPACITY / 4)))

        self.__inspectorBee = InspectorBee()


    def __assignBeesToCells(self) -> list[BeeAssignment]:
        bee_assignments: list[BeeAssignment] = []

        for i in range(len(self.__employedBees)):
            bee_assignments.append(BeeAssignment(self.__employedBees[i],  self.__pickCellToFly()))
        
        return bee_assignments


    def __setQualityToCell(self, cell: Cell, quality: float) -> None:
        for i in range(0, len(self.__cellsQualityTable)):
            if self.__cellsQualityTable[i].cell == cell:
                self.__cellsQualityTable[i].quality = quality


    def __pickCellToFly(self) -> Cell or None:
        sortedQualityTable = sorted(self.__cellsQualityTable, key=lambda x: x.quality, reverse=True)

        for i in range(len(sortedQualityTable)):
            cell: Cell = sortedQualityTable[i].cell

            if cell.value == 0: 
                continue

            return cell