import random


class TaskType:
    BACKEND = 'backend'
    FRONTEND = 'frontend'
    MOBILE = 'mobile'


class TaskState:
    TODO = 'todo'
    IN_PROGRESS = 'in_progress'
    NEEDS_REVIEW = 'needs_review'
    READY_FOR_STAGE = 'ready_for_stage'
    STAGE = 'stage'
    READY_FOR_PROD = 'ready_for_prod'
    PROD = 'prod'


class Task:
    def __init__(self, name, task_type):
        self.name = name
        self.task_type = task_type
        self.state = TaskState.TODO


class Product:
    def __init__(self, tasks):
        self.tasks = tasks


class ProductOwner:
    def create_product(self):
        tasks = [
            Task('b-0', TaskType.BACKEND),
            Task('b-1', TaskType.BACKEND),
            Task('b-2', TaskType.BACKEND),
            Task('b-3', TaskType.BACKEND),
            Task('f-0', TaskType.FRONTEND),
            Task('f-1', TaskType.FRONTEND),
            Task('f-2', TaskType.FRONTEND),
            Task('f-3', TaskType.FRONTEND),
            Task('m-0', TaskType.MOBILE),
            Task('m-1', TaskType.MOBILE),
            Task('m-2', TaskType.MOBILE)
        ]
        return Product(tasks)

    def is_task_complete(self, task):
        task_completion = random.randint(0, 100)
        return task_completion % 30 != 0


class Developer:
    def __init__(self):
        self.tasks = []

    def assign_tasks(self, tasks):
        self.tasks.extend(tasks)

    def perform_tasks(self):
        for task in self.tasks:
            self.perform_task(task)

    def perform_task(self, task):
        task.state = TaskState.IN_PROGRESS
        print(f"{self.__class__.__name__}: Working on task '{task.name}'")

        if self.check_task_completion(task):
            task.state = TaskState.NEEDS_REVIEW
            print(f"{self.__class__.__name__}: Completed task '{task.name}'")
        else:
            task.state = TaskState.TODO
            print(f"{self.__class__.__name__}: Failed to complete task '{task.name}'")

    def check_task_completion(self, task):
        raise NotImplementedError("Subclasses must implement the 'check_task_completion' method.")


class BackendDeveloper(Developer):
    def check_task_completion(self, task):
        return random.randint(1, 10) > 2


class FrontendDeveloper(Developer):
    def check_task_completion(self, task):
        return random.randint(1, 10) > 3


class MobileDeveloper(Developer):
    def check_task_completion(self, task):
        return random.randint(1, 10) > 4


class Lead:
    def review_task(self, task):
        task.state = TaskState.IN_PROGRESS
        print(f"Lead: Reviewing task '{task.name}'")

        if random.randint(1, 10) > 4:
            task.state = TaskState.READY_FOR_STAGE
            print(f"Lead: Task '{task.name}' approved")
        else:
            task.state = TaskState.TODO
            print(f"Lead: Task '{task.name}' rejected")


class QA:
    def test_task(self, task):
        task.state = TaskState.STAGE
        print(f"QA: Testing task '{task.name}'")

        if random.randint(1, 10) > 4:
            task.state = TaskState.READY_FOR_PROD
            print(f"QA: Task '{task.name}' passed testing")
        else:
            task.state = TaskState.NEEDS_REVIEW
            print(f"QA: Task '{task.name}' failed testing")


class DevOps:
    def deploy_to_stage(self, task):
        task.state = TaskState.STAGE
        print(f"DevOps: Deploying task '{task.name}' to stage")

    def deploy_to_prod(self, task):
        task.state = TaskState.PROD
        print(f"DevOps: Deploying task '{task.name}' to production")


class Team:
    def __init__(self, product_owner):
        self.product_owner = product_owner
        self.developers = []
        self.lead = None
        self.qa = None
        self.devops = None

    def run(self):
        self.create_team()

        product = self.product_owner.create_product()

        backend_tasks = [task for task in product.tasks if task.task_type == TaskType.BACKEND]
        frontend_tasks = [task for task in product.tasks if task.task_type == TaskType.FRONTEND]
        mobile_tasks = [task for task in product.tasks if task.task_type == TaskType.MOBILE]

        random.shuffle(backend_tasks)
        random.shuffle(frontend_tasks)
        random.shuffle(mobile_tasks)

        self.assign_tasks_to_developers(backend_tasks, self.get_backend_developers())
        self.assign_tasks_to_developers(frontend_tasks, self.get_frontend_developers())
        self.assign_tasks_to_developers(mobile_tasks, self.get_mobile_developers())

        for task in product.tasks:
            if task.state == TaskState.TODO:
                self.get_lead().review_task(task)

        staged_tasks = [task for task in product.tasks if task.state == TaskState.READY_FOR_STAGE]
        for task in staged_tasks:
            self.get_qa().test_task(task)

        for task in product.tasks:
            if task.state == TaskState.READY_FOR_PROD:
                self.get_devops().deploy_to_prod(task)

        print("Product development completed.")

    def get_backend_developers(self):
        return [dev for dev in self.developers if isinstance(dev, BackendDeveloper)]

    def get_frontend_developers(self):
        return [dev for dev in self.developers if isinstance(dev, FrontendDeveloper)]

    def get_mobile_developers(self):
        return [dev for dev in self.developers if isinstance(dev, MobileDeveloper)]

    def assign_tasks_to_developers(self, tasks, developers):
        num_tasks = len(tasks)
        num_developers = len(developers)
        num_iterations = min(num_tasks, num_developers)

        for i in range(num_iterations):
            developers[i].assign_tasks([tasks[i]])

    def create_team(self):
        self.lead = Lead()
        self.qa = QA()
        self.devops = DevOps()

        num_backend_developers = random.randint(1, 3)
        num_frontend_developers = random.randint(1, 3)
        num_mobile_developers = random.randint(1, 3)

        for _ in range(num_backend_developers):
            self.developers.append(BackendDeveloper())

        for _ in range(num_frontend_developers):
            self.developers.append(FrontendDeveloper())

        for _ in range(num_mobile_developers):
            self.developers.append(MobileDeveloper())

    def get_lead(self):
        return self.lead

    def get_qa(self):
        return self.qa

    def get_devops(self):
        return self.devops


def main():
    product_owner = ProductOwner()
    team = Team(product_owner)
    team.run()


if __name__ == '__main__':
    main()
