from Model import DevelopmentTaskAdapter, TestingTask, EngineerAdapter
# Controlador
class TimeTrackerController:
    def __init__(self):
        self.tasks = []
        self.engineers = []
    
    def create_development_task(self, name, state=0):
        task = DevelopmentTaskAdapter(name, state)
        self.tasks.append(task)
    
    def create_testing_task(self, name, state=0):
        task = TestingTask(name, state)
        self.tasks.append(task)
    
    def assign_developer(self, name, role):
        engineer = EngineerAdapter(name, role)
        self.engineers.append(engineer)

    def assign_tester(self, name, role):
        engineer = EngineerAdapter(name, role)
        self.engineers.append(engineer)
