# Реалізація шаблону спостерігача
class Observable:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)


# Базовий клас для всіх членів команди
class TeamMember:
    def __init__(self, name):
        self.name = name


# Конкретні члени команди
class Developer(TeamMember):
    def develop(self, software):
        print(f"{self.name} is developing {software.name}")


class SoftwareArchitect(TeamMember):
    def architect(self, software):
        print(f"{self.name} is architecting {software.name}")


class TeamLead(TeamMember):
    def lead(self, team):
        print(f"{self.name} is leading the {team} team")


class QA(TeamMember):
    def test(self, software):
        print(f"{self.name} is testing {software.name}")


class BusinessAnalyst(TeamMember):
    def analyze(self, requirements):
        print(f"{self.name} is analyzing {requirements}")


# Реалізація паттерну
class Software:
    def __init__(self, name):
        self.name = name
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def remove_component(self, component):
        self.components.remove(component)

    def develop(self):
        print(f"Developing {self.name}:")
        for component in self.components:
            component.develop(self.name)

    def test(self):
        print(f"Testing {self.name}:")
        for component in self.components:
            component.test(self.name)


# Конкретні програмні компоненти
class MobileApp:
    def develop(self, software):
        print(f"Developing mobile app for {software}")

    def test(self, software):
        print(f"Testing mobile app for {software}")


class WebApp:
    def develop(self, software):
        print(f"Developing web app for {software}")

    def test(self, software):
        print(f"Testing web app for {software}")


class DatabaseAPI:
    def develop(self, software):
        print(f"Developing database API for {software}")

    def test(self, software):
        print(f"Testing database API for {software}")


class Containerization:
    def develop(self, software):
        print(f"Performing containerization for {software}")

    def test(self, software):
        print(f"Testing containerization for {software}")


class Deployment:
    def develop(self, software):
        print(f"Performing deployment for {software}")

    def test(self, software):
        print(f"Testing deployment for {software}")


# Приклад використання
if __name__ == "__main__":
    # Створення команди проекту
    developer1 = Developer("Misha")
    developer2 = Developer("George")
    architect = SoftwareArchitect("Sasha")
    team_lead = TeamLead("Volodya")
    qa = QA("Anton")
    business_analyst = BusinessAnalyst("Anna")

    # Створення програмних компонентів
    mobile_app = MobileApp()
    web_app = WebApp()
    database_api = DatabaseAPI()
    containerization = Containerization()
    deployment = Deployment()

    # Створення програмного забезпечення
    software = Software("Project X")
    software.add_component(mobile_app)
    software.add_component(web_app)
    software.add_component(database_api)
    software.add_component(containerization)
    software.add_component(deployment)

    # Розподілення обов'язків
    developer1.develop(software)
    developer2.develop(software)
    architect.architect(software)
    team_lead.lead("development")
    qa.test(software)
    business_analyst.analyze("requirements")

    # Розробка і тест проекту
    software.develop()
    software.test()