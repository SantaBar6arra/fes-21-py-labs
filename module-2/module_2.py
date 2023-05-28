import random
from enum import Enum


class TaskType(Enum):
    BACKEND = 0
    FRONTEND = 1
    MOBILE = 2

class TaskState(Enum):
    TODO = 0
    INPROGRESS = 1
    NEEDSREVIEW = 2
    READYFORSTAGE = 3
    STAGE = 4
    READYFORPROD = 5
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

class Employee:
    pass

class Dev(Employee):
    current_task: Task

    def AssignTask(self, task: Task):
        self.current_task = task

    def DoTask(self):
        pass

    def IsTaskAsigned(self) -> bool:
        return self.current_task != None

class Lead(Employee):
    def Review(self, task: Task) -> bool:
        if not self.IsTaskDoneProperly(task):
            task.state = TaskState.TODO
            print(f'LEAD - Task {task.name} failed review')
        else:
            task.state = TaskState.READYFORSTAGE
            print(f'LEAD - Task {task.name} passed review and is ready for stage')

    def IsTaskDoneProperly(self, _: Task) -> bool:
        task_completance = random.randint(1, 100)
        return task_completance % 5 != 0
    
class BackendDev(Dev):
    def DoTask(self):
        if not super().IsTaskAsigned(): return
        self.current_task.state = TaskState.INPROGRESS
        print(f'BACKEND DEV - Backend task {self.current_task.name} is in progress')
        self.current_task.state = TaskState.NEEDSREVIEW
        print(f'BACKEND DEV - Backend task {self.current_task.name} is prepared for review')
        self.current_task = None

class FrontendDev(Dev):
    def DoTask(self): 
        if not super().IsTaskAsigned(): return
        self.current_task.state = TaskState.INPROGRESS
        print(f'FRONTEND DEV - Frontend task {self.current_task.name} is in progress')
        self.current_task.state = TaskState.NEEDSREVIEW
        print(f'FRONTEND DEV - Frontend task {self.current_task.name} is prepared for review')
        self.current_task = None
        
class MobileDev(Dev):
    def DoTask(self): 
        if not super().IsTaskAsigned(): return
        self.current_task.state = TaskState.INPROGRESS
        print(f'MOBILE DEV - Mobile task {self.current_task.name} is in progress')
        self.current_task.state = TaskState.NEEDSREVIEW
        print(f'MOBILE DEV - Mobile task {self.current_task.name} is prepared for review')
        self.current_task = None

class QA(Employee):
    def test(self, task: Task): 
        if not self.IsTaskDoneProperly(task): 
            task.state = TaskState.TODO
            print(f'QA - Task {task.name} failed testing')
        else:
            task.state = TaskState.READYFORPROD
            print(f'QA - Task {task.name} passed testing and is ready for prod')

    def IsTaskDoneProperly(self, _: Task) -> bool:
        task_completance = random.randint(1, 100)
        return task_completance % 10 != 0

class DevOps(Employee):
    def DeployToStage(self, task: Task): 
        task.state = TaskState.STAGE
        print(f'DEVOPS - Deployed task {task.name} to stage')

    def DeployToProd(self, task: Task):
        task.state = TaskState.PROD
        print(f'DEVOPS - Deployed task {task.name} to prod')


class Owner:
    def CreateProduct(self) -> Product:

        return Product([
            Task('BACKEND-0', TaskType.BACKEND),    Task('BACKEND-1', TaskType.BACKEND),    Task('BACKEND-2', TaskType.BACKEND),    Task('BACKEND-3', TaskType.BACKEND),
            Task('FRONTEND-0', TaskType.FRONTEND),  Task('FRONTEND-1', TaskType.FRONTEND),  Task('FRONTEND-2', TaskType.FRONTEND),  Task('FRONTEND-3', TaskType.FRONTEND),  Task('FRONTEND-4', TaskType.FRONTEND),
            Task('MOBILE-1', TaskType.MOBILE),      Task('MOBILE-2', TaskType.MOBILE),      Task('MOBILE-3', TaskType.MOBILE)])

    def Check(self, _: Task) -> bool:
        task_completancy = random.randint(0, 100)
        return task_completancy % 30 != 0


class Team:
    devs: list[Dev] = list[Dev]()
    lead: Lead
    qa: QA
    devops: DevOps
    owner: Owner
    product: Product 

    def __init__(self, owner: Owner) -> None:
        self.owner = owner
        self.product = owner.CreateProduct()
        self.CreateTeam()

    def Run(self):
        BackendDevs  = [d for d in self.devs if d.__class__ == BackendDev]
        FrontendDevs = [d for d in self.devs if d.__class__ == FrontendDev]
        MobileDevs   = [d for d in self.devs if d.__class__ == MobileDev]
        IsProjectComplete = False

        while not IsProjectComplete:
            ToDoBackendTasks  = [t for t in self.product.features if t.state == TaskState.TODO and t.type == TaskType.BACKEND]
            ToDoFrontendTasks = [t for t in self.product.features if t.state == TaskState.TODO and t.type == TaskType.FRONTEND]
            ToDoMobileTasks   = [t for t in self.product.features if t.state == TaskState.TODO and t.type == TaskType.MOBILE]

            self.AssignTasksToDevs(ToDoBackendTasks, BackendDevs)
            self.AssignTasksToDevs(ToDoFrontendTasks, FrontendDevs)
            self.AssignTasksToDevs(ToDoMobileTasks, MobileDevs)
            for dev in self.devs:
                dev.DoTask()

            self.Review()
            self.Deploy(TaskState.READYFORSTAGE)
            self.Test()
            self.Deploy(TaskState.READYFORPROD)
            self.OwnerReview()
            IsProjectComplete = len([t for t in self.product.features if t.state != TaskState.PROD]) == 0

    def OwnerReview(self):
        tasks_on_prod = [t for t in self.product.features if t.state == TaskState.PROD]
        for task in tasks_on_prod:
            is_task_approved_by_owner = self.owner.Check(task)

            if not is_task_approved_by_owner:
                print(f'OWNER - Owner rejected {task.name}')
                task.state = TaskState.TODO
            else: 
                print(f'OWNER - Task {task.name} approved')

    def Review(self):
        tasks_to_review = [t for t in self.product.features if t.state == TaskState.NEEDSREVIEW]
        for task_to_review in tasks_to_review:
            self.lead.Review(task_to_review)

    def Deploy(self, state: TaskState):
        if state != TaskState.READYFORSTAGE and state != TaskState.READYFORPROD:
            raise ValueError('Invalid state error')
        
        tasks_to_deploy = [t for t in self.product.features if t.state == state]
        if state == TaskState.READYFORSTAGE:
            for task in tasks_to_deploy:
                self.devops.DeployToStage(task)
        elif state == TaskState.READYFORPROD:
            for task in tasks_to_deploy:
                self.devops.DeployToProd(task)

    def Test(self):
        staged_tasks = [t for t in self.product.features if t.state == TaskState.STAGE]
        for staged_task in staged_tasks:
            self.qa.test(staged_task)

    def AssignTasksToDevs(self, tasks: list[Task], devs: list[Dev]):
        if len(tasks) >= len(devs):
            for i in range(len(devs)):
                devs[i].AssignTask(tasks[i])
        else:
            for i in range(len(tasks)):
                devs[i].AssignTask(tasks[i])

    def CreateTeam(self):
        self.lead = Lead()
        self.devops = DevOps()
        self.qa = QA()

        for _ in range(random.randint(1, 3)): self.devs.append(BackendDev())
        for _ in range(random.randint(1, 3)): self.devs.append(FrontendDev())
        for _ in range(random.randint(1, 3)): self.devs.append(MobileDev())




owr = Owner()
t = Team(owr)
t.Run()