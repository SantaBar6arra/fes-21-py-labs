from fastapi import FastAPI
from config import Config
from hive import Hive


app = FastAPI()

@app.post('/hive')
async def run_hive(config: Config):
    hive = Hive(config)
    return hive.run()
