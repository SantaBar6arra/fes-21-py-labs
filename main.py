# Класи розробників

class Developer:
    def __init__(self, name):
        self.name = name

    def write_code(self):
        print(f"{self.name} is writing code.")


class SoftwareArchitect(Developer):
    def __init__(self, name):
        super().__init__(name)

    def design_software(self):
        print(f"{self.name} is designing software.")


class TeamLead(Developer):
    def __init__(self, name):
        super().__init__(name)

    def coordinate_team(self):
        print(f"{self.name} is coordinating the team.")


class QA(Developer):
    def __init__(self, name):
        super().__init__(name)

    def test_software(self):
        print(f"{self.name} is testing the software.")


class BusinessAnalyst:
    def __init__(self, name):
        self.name = name

    def analyze_requirements(self):
        print(f"{self.name} is analyzing requirements.")


# Класи програмного забезпечення

class Software:
    def develop(self):
        raise NotImplementedError("Subclasses must implement this method.")


class MobileApp(Software):
    def develop(self):
        print("Developing Mobile App.")


class Android(MobileApp):
    def develop(self):
        print("Developing Android App.")


class IOS(MobileApp):
    def develop(self):
        print("Developing iOS App.")


class WebApp(Software):
    def develop(self):
        raise NotImplementedError("Subclasses must implement this method.")


class JSBackend(WebApp):
    def develop(self):
        print("Developing JS Backend.")


class PythonBackend(WebApp):
    def develop(self):
        print("Developing Python Backend.")


class JSFrontend(WebApp):
    def develop(self):
        print("Developing JS Frontend.")


class DatabaseAPI(Software):
    def develop(self):
        print("Developing Database API.")


class Containerization(Software):
    def develop(self):
        print("Performing Containerization.")


class Deployment(Software):
    def develop(self):
        print("Performing Deployment.")


# Приклад використання

if __name__ == "__main__":
    # Створення команди розробників
    developer1 = Developer("John")
    developer2 = Developer("Alice")
    architect = SoftwareArchitect("Bob")
    team_lead = TeamLead("Mike")
    qa = QA("Sarah")

    # Виклик методів для виконання обов'язків розробників
    developer1.write_code()
    developer2.write_code()
    architect.design_software()
    team_lead.coordinate_team()
    qa.test_software()

    # Створення програмного забезпечення
    mobile_app = Android()
    web_app = PythonBackend()
    database_api = DatabaseAPI()
    containerization = Containerization()
    deployment = Deployment()

    # Виклик методів для розробки програмного забезпечення
    mobile_app.develop()
    web_app.develop()
    database_api.develop()
    containerization.develop()
    deployment.develop()
