import product
import random


class Employee:
    pass


class Dev(Employee):
    current_task: product.Task

    def assign_task(self, task: product.Task):
        self.current_task = task

    def do_task(self):
        pass

    def is_task_assigned(self) -> bool: # todo: make it private
        return self.current_task != None


class BackendDev(Dev):
    def do_task(self):
        if not super().is_task_assigned(): return
        self.current_task.state = product.TaskState.IN_PROGRESS
        print(f'backend dev: backend task {self.current_task.name} is in progress')
        self.current_task.state = product.TaskState.NEEDS_REVIEW
        print(f'backend dev: backend task {self.current_task.name} is prepared for review')
        self.current_task = None
        

class MobileDev(Dev):
    def do_task(self): 
        if not super().is_task_assigned(): return
        self.current_task.state = product.TaskState.IN_PROGRESS
        print(f'mobile dev: mobile task {self.current_task.name} is in progress')
        self.current_task.state = product.TaskState.NEEDS_REVIEW
        print(f'mobile dev: mobile task {self.current_task.name} is prepared for review')
        self.current_task = None


class FrontendDev(Dev):
    def do_task(self): 
        if not super().is_task_assigned(): return
        self.current_task.state = product.TaskState.IN_PROGRESS
        print(f'frontend dev: frontend task {self.current_task.name} is in progress')
        self.current_task.state = product.TaskState.NEEDS_REVIEW
        print(f'frontend dev: frontend task {self.current_task.name} is prepared for review')
        self.current_task = None


class Lead(Employee):
    def review(self, task: product.Task) -> bool:
        if not self.__is_task_done_properly(task):
            task.state = product.TaskState.TODO
            print(f'lead: task {task.name} failed review')
        else:
            task.state = product.TaskState.READY_FOR_STAGE
            print(f'lead: task {task.name} passed review and is ready for stage')

    def __is_task_done_properly(self, _: product.Task) -> bool:
        task_completance = random.randint(1, 100)
        return task_completance % 5 != 0


class QA(Employee):
    def test(self, task: product.Task): 
        if not self.__is_task_done_properly(task): 
            task.state = product.TaskState.TODO
            print(f'qa: task {task.name} failed testing')
        else:
            task.state = product.TaskState.READY_FOR_PROD
            print(f'qa: task {task.name} passed testing and is ready for prod')

    def __is_task_done_properly(self, _: product.Task) -> bool:
        task_completance = random.randint(1, 100)
        return task_completance % 10 != 0


class DevOps(Employee):
    def deploy_to_stage(self, task: product.Task): 
        task.state = product.TaskState.STAGE
        print(f'devops: deployed task {task.name} to stage')

    def deploy_to_prod(self, task: product.Task):
        task.state = product.TaskState.PROD
        print(f'devops: deployed task {task.name} to prod')
    
    # def setup_cicd(): print('ci/cd enabled')
