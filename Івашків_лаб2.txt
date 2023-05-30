import random
import math

class Config:
    height = 10
    width = 10
    food_range = (10, 50)
    employed_bees_count = 5
    inspector_bees_count = 2
    food_limit = 3

class Hive:
    def __init__(self):
        self.food_bank = {}

    def upload_food(self, food):
        for source, amount in food.items():
            if source in self.food_bank:
                self.food_bank[source] += amount
            else:
                self.food_bank[source] = amount

class EmployedBee:
    def __init__(self):
        self.food_amount = random.randint(1, Config.food_range[1] - 1)

    def fly(self, source):
        distance = math.sqrt(source[0] ** 2 + source[1] ** 2)
        return distance

    def gather(self, source):
        food_collected = min(self.food_amount, Config.food_bank[source])
        self.food_amount -= food_collected
        Config.food_bank[source] -= food_collected
        return food_collected

class InspectorBee:
    def __init__(self):
        pass

    def check_quality(self, food_sources, employed_bees):
        quality_values = {}
        for source in food_sources:
            total_food = sum([bee.gather(source) for bee in employed_bees])
            distance = math.sqrt(source[0] ** 2 + source[1] ** 2)
            source_quality = random.random() * total_food / distance
            quality_values[source] = source_quality
        return quality_values

def generate_coordinate_grid():
    grid = []
    for x in range(Config.width + 1):
        for y in range(Config.height + 1):
            grid.append([x, y])
    return grid

def generate_food_sources():
    sources = random.sample(generate_coordinate_grid(), Config.employed_bees_count)
    food_sources = {}
    for source in sources:
        food_sources[tuple(source)] = random.randint(*Config.food_range)
    return food_sources

def main():
    hive = Hive()
    Config.food_bank = {}
    food_sources = generate_food_sources()
    employed_bees = [EmployedBee() for _ in range(Config.employed_bees_count)]
    inspector_bees = [InspectorBee() for _ in range(Config.inspector_bees_count)]

    iteration = 1

    while food_sources:
        print(f"Iteration {iteration}")
        print("Food Sources:", food_sources)

        for bee in employed_bees:
            source = random.choice(list(food_sources.keys()))
            distance = bee.fly(source)
            if distance > 0:
                food_collected = bee.gather(source)
                hive.upload_food({source: food_collected})
            if source not in food_sources:
                continue
            if Config.food_bank[source] == 0:
                del food_sources[source]

        quality_values = inspector_bees[0].check_quality(list(food_sources.keys()), employed_bees)
        print("Quality Values:", quality_values)

        print("Food Bank:", hive.food_bank)

        iteration += 1

main()