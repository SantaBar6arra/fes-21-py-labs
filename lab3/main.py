import numpy as np

from bs4 import BeautifulSoup
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from jinja2 import Template
from datetime import datetime

from HiveModule.bees import *
from HiveModule.field import *

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/simulation-json")
async def run_simulation(size: tuple[int, int] = (100, 100),
                         food_sources_count: int = 5, employed_bees_count: int = 5,
                         min_food_amout: int = 1, max_food_amout: int = 10):
    hive = Hive()
    field = Field(size[0], size[1])

    simulation_log = []

    # Create food sources
    total_food_amout = 0
    for i in range(food_sources_count):
        x, y = np.random.randint(0, field.width), np.random.randint(0, field.height)
        field.food_sources.append(FoodSource((x, y), np.random.randint(min_food_amout, max_food_amout)))
        total_food_amout += field.food_sources[-1].food_amount

    simulation_log.append(f"Starting simulation at {datetime.now()}")
    simulation_log.append(f"Total food amout: {total_food_amout}")

    # Create employed bees
    for i in range(employed_bees_count):
        hive.employed_bees.append(EmployedBee(i))

    # Create inspector bee
    hive.inspector_bee = InspectorBee()

    while hive.food_bank < total_food_amout:
        food_source_index = 0
        for bee in hive.employed_bees:
            if field.food_sources[food_source_index].honey_quality > 0:
                food_source = field.food_sources[food_source_index]
                bee.fly(food_source.position, food_source)
                simulation_log.append(f"Employed bee {bee.id} flew to food source {food_source.position}")
                food_source_index += 1
            else:
                food_source_index = 0

        for bee in hive.employed_bees:
            if bee.target_food_source is not None:
                gathered_food, food_source = bee.gather()
                simulation_log.append(
                    f"Employed bee {bee.id} gathered {gathered_food} food from food source {food_source.position}")

        for bee in hive.employed_bees:
            bee.fly((0, 0))
            simulation_log.append(f"Employed bee {bee.id} flew to hive")
            bee.upload_food(hive)

        simulation_log.append(f"All food uploaded to hive")
        simulation_log.append(f"Hive has {hive.food_bank} food in the bank.")

        for source in field.food_sources:
            source.honey_quality = hive.inspector_bee.check_honey(source, source.taken_food)
            source.taken_food = 0
            simulation_log.append(
                f"Inspector bee checked food source {source.position} and found honey quality {source.honey_quality}")

        field.food_sources.sort(key=lambda variable: variable.honey_quality, reverse=True)

    simulation_log.append(f"Hive has {hive.food_bank} food in the bank.")
    simulation_log.append(f"Simulation ended at {datetime.now()}")

    response = {
        "log": simulation_log,
        "code": 200
    }

    return response


@app.get("/simulation", response_class=HTMLResponse)
async def simulation(request: Request):
    simulation_log = (await run_simulation()).get("log")
    tag = "p"
    dynamic_content = f"<{tag}>" + f"</{tag}><{tag}>".join(simulation_log) + f"/<{tag}>"

    template = Template(open("templates/simulation.html").read())
    rendered_template = template.render(request=request, dynamic_content=dynamic_content)

    return rendered_template

@app.get("/")
async def root(request: Request):
    dynamic_content = "Dynamic content: " + str(datetime.now())
    root_file = open("templates/root.html", "r+")
    root_soup = BeautifulSoup(root_file, "html.parser")
    root_soup.find("p", {"class": "dynamic-content"}).string = dynamic_content
    root_file.seek(0)
    root_file.write(str(root_soup))
    root_file.close()
    return templates.TemplateResponse(
        "root.html",
        {
            "request": request,
        })
