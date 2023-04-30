import random
from helper import ab_distance


class Hive:
    """A hive where bees live and work."""
    def __init__(self):
        self.position = (0, 0)
        self.food_bank = 0
        self.employed_bees = []
        self.inspector_bee = None


class EmployedBee:
    """A bee that works for the hive"""
    def __init__(self):
        self.position = (0, 0)
        self.max_food_amout = random.randint(1, 10)
        self.food_amout = 0
        self.target_food_source = None

    def fly(self, position, food_source=None):
        # This function makes the bee fly to the source
        self.position = position
        self.target_food_source = food_source
        if food_source is not None:
            print(f"Employed bee is now at {self.position}.")

    def gather(self):
        self.food_amout = min(self.max_food_amout, self.target_food_source.food_amount)
        self.target_food_source.food_amount -= self.food_amout
        self.target_food_source.taken_food += self.food_amout
        self.target_food_source = None
        print(f"Employed bee gathered {self.food_amout} food from {self.position}.")
            
    def upload_food(self, hive):
        hive.food_bank += self.food_amout
        self.food_amout = 0
        print(f"Hive now has {hive.food_bank} food in the bank.")


class InspectorBee:
    """A bee that checks the quality of the honey"""
    def __init__(self):
        pass

    def check_honey(self, source, all_taken_food) -> float:
        """Check the quality of the honey in the source.
        Return a number between 0 and 1, where 0 is the worst and 1 is the best.
        NOT IMPLEMENTED"""
        source_quality = random.random() * all_taken_food / ab_distance((0, 0), source.position)
        print(f"Inspector bee checked honey quality in {source.position} and found {source_quality}.")
        return source_quality
