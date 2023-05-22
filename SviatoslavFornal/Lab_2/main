import random
import math

class Config:
    height = 10
    width = 10
    food_source_range = (10, 20)
    food_source_limit = 3
    employed_bees = 5
    employed_bee_food_amount_range = (1, 5)
    inspector_bees = 2

class Hive:
    def init(self):
        self.food_bank = {}

    def upload_food(self, food):
        for source, amount in food.items():
            if source in self.food_bank:
                self.food_bank[source] += amount
            else:
                self.food_bank[source] = amount

class EmployedBee:
    def init(self, food_amount):
        self.food_amount = food_amount
        self.current_location = (0, 0)
        self.target_food_source = None
        self.food = {}

    def fly(self, source):
        self.current_location = (0, 0)
        self.target_food_source = source

    def gather(self):
        if self.target_food_source is not None:
            distance = math.sqrt((self.target_food_source[0] - self.current_location[0])**2 +
                                 (self.target_food_source[1] - self.current_location[1])**2)
            amount = min(self.food_amount, self.target_food_source[1])
            self.target_food_source = (self.target_food_source[0], self.target_food_source[1] - amount)
            self.food[self.target_food_source] = amount
            self.current_location = self.target_food_source[0]
            self.target_food_source = None

class InspectorBee:
    def init(self):
        self.quality_scores = {}

    def evaluate_food_source(self, source, bees):
        if source not in self.quality_scores:
            taken_food = sum([bee.food.get(source, 0) for bee in bees])
            distance = math.sqrt(source[0]**2 + source[1]**2)
            self.quality_scores[source] = random.random() * taken_food / distance

def generate_coordinate_grid():
    return [[i, j] for i in range(Config.width) for j in range(Config.height)]

def generate_food_sources(grid):
    sources = random.sample(grid, Config.food_source_limit)
    food_sources = {}
    for source in sources:
        food_sources[tuple(source)] = random.randint(*Config.food_source_range)
    return food_sources

def main():
    hive = Hive()
    bees = [EmployedBee(random.randint(*Config.employed_bee_food_amount_range)) for _ in range(Config.employed_bees)]
    inspectors = [InspectorBee() for _ in range(Config.inspector_bees)]
    grid = generate_coordinate_grid()
    food_sources = generate_food_sources(grid)

    while food_sources:
        for bee in bees:
            if bee.target_food_source is None:
                sources = [source for source in food_sources if food_sources[source] > 0]
                if sources:
                    bee.fly(random.choice(sources))
            else:
                bee.gather()
                if bee.target_food_source not in food_sources or food_sources[bee.target_food_source] <= 0:
                    sources = [source for source in food_sources if food_sources[source] > 0]
                    if sources:
                        bee.fly(random.choice(sources))
                    else:
                        continue
                for inspector in inspectors:
                    inspector.evaluate_food_source(bee.target_food_source, bees)
        for inspector in inspectors:
            sorted_sources = sorted(inspector.quality_scores, key=inspector.quality_scores.get, reverse=True)
            for source in sorted_sources:
                if source in food_sources and food_sources[source] > 0:
                    taken_food = sum([bee.food.get(source, 0) for bee in bees])
                    if taken_food >= Config.food_source_range[1]:
                        food_sources.pop(source)
                        hive.upload_food({source: taken_food})
                        break
                    else:
                        for bee in bees:
                            if bee.target_food_source == source and food_sources[source] > 0:
                                bee.gather()
                                break
    print("All food sources have been exhausted.")
