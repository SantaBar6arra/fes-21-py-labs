from config import Config
from hive import Hive


hive: Hive = Hive(Config())

hive.run()
