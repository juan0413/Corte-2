class Task:
    def __init__(self, name, state):
        self.name = name
        self.state = state

class DevelopmentTask(Task):
    states = ['Inicio', 'Ejecución', 'Finalizado']
    def __init__(self, name, state=0):
        super().__init__(name, state)

class TestingTask(Task):
    states = ['Propuesta', 'En prueba', 'Certificada', 'Devolver']
    def __init__(self, name, state=0):
        super().__init__(name, state)

class Engineer:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        
# Adaptador para ingenieros
class EngineerAdapter(Engineer):
    def __init__(self, name, role):
        super().__init__(name, role)

    def __str__(self):
        return f"{self.name} - {self.role}"

# Adaptador para las tareas de desarrollo
class DevelopmentTaskAdapter(Task):
    def __init__(self, name, state=0):
        super().__init__(name, state)
    
    def get_state(self):
        return DevelopmentTask.states[self.state]
