import random
from helper import ab_distance


class Hive:
    def __init__(self):
        self.position = (0, 0)
        self.food_bank = 0
        self.employed_bees = []
        self.inspector_bee = None


class EmployedBee:
    def __init__(self):
        self.position = (0, 0)
        self.max_food_amount = random.randint(1, 10)
        self.food_amount = 0
        self.target_food_source = None

    def fly(self, position, food_source=None):
        self.position = position
        self.target_food_source = food_source
        if food_source is not None:
            print(f"Employed bee is now at {self.position}.")

    def gather(self):
        self.food_amount = min(self.max_food_amount, self.target_food_source.food_amount)
        self.target_food_source.food_amount -= self.food_amount
        self.target_food_source.taken_food += self.food_amount
        self.target_food_source = None
        print(f"Employed bee gathered {self.food_amount} food from {self.position}.")

    def upload_food(self, hive):
        hive.food_bank += self.food_amount
        self.food_amount = 0
        print(f"Hive now has {hive.food_bank} food in the bank.")


class InspectorBee:
    def __init__(self):
        pass

    def check_honey(self, source, all_taken_food) -> float:
        source_quality = random.random() * all_taken_food / ab_distance((0, 0), source.position)
        print(f"Inspector bee checked honey quality in {source.position} and found {source_quality}.")
        return source_quality