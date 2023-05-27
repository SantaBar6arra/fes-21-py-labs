import numpy as np
from bees import *
from field import *
from time import sleep


def run(size=(100, 100), food_sources_count=5, employed_bees_count=5, min_food_amount=1, max_food_amount=10):
    hive = Hive()
    field = Field(100, 100)

    food_sources_count = 5
    total_food_amount = 0
    for i in range(food_sources_count):
        x, y = np.random.randint(0, field.width), np.random.randint(0, field.height)
        field.food_sources.append(FoodSource((x, y), np.random.randint(min_food_amount, max_food_amount)))
        total_food_amount += field.food_sources[-1].food_amount

    print(f"Total food amount: {total_food_amount}")

    employed_bees_count = 5
    for i in range(employed_bees_count):
        hive.employed_bees.append(EmployedBee())

    hive.inspector_bee = InspectorBee()

    while hive.food_bank < total_food_amount:
        sleep(1)

        food_source_index = 0
        for bee in hive.employed_bees:
            if field.food_sources[food_source_index].honey_quality > 0:
                food_source = field.food_sources[food_source_index]
                bee.fly(food_source.position, food_source)
                food_source_index += 1
            else:
                food_source_index = 0

        for bee in hive.employed_bees:
            if bee.target_food_source is not None:
                bee.gather()

        for bee in hive.employed_bees:
            bee.fly((0, 0))
            bee.upload_food(hive)

        for source in field.food_sources:
            source.honey_quality = hive.inspector_bee.check_honey(source, source.taken_food)
            source.taken_food = 0

        field.food_sources.sort(key=lambda source: source.honey_quality, reverse=True)

    print("Simulation ended.")
    print(f"Hive has {hive.food_bank} food in the bank.")


if __name__ == "__main__":
    run((100, 100), 5, 5, 10, 50)