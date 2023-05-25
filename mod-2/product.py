from enum import Enum


class TaskType(Enum):
    BACKEND = 0
    FRONTEND = 1
    MOBILE = 2


class TaskState(Enum):
    TODO = 0
    IN_PROGRESS = 1
    NEEDS_REVIEW = 2
    READY_FOR_STAGE = 3
    STAGE = 4
    READY_FOR_PROD = 5
    PROD = 6


class Task:
    name: str
    type: TaskType
    state: TaskState

    def __init__(self, name: str, type: TaskType) -> None:
        self.name = name
        self.type = type
        self.state = TaskState.TODO


class Product:
    features: list[Task]

    def __init__(self, features: list[Task]) -> None:
        self.features = features
