from Controller import TimeTrackerController
class TimeTrackerView:
    def display_tasks(self, tasks):
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.name} - {task.state}")

    def display_engineers(self, engineers):
        for i, engineer in enumerate(engineers, 1):
            print(f"{i}. {engineer}")

# Uso
if __name__ == "__main__":
    controller = TimeTrackerController()
    view = TimeTrackerView()

    controller.create_development_task("Desarrollo 1")
    controller.create_development_task("Desarrollo 2", state=1)
    controller.create_testing_task("Testing 1")

    controller.assign_developer("Juan", "Desarrollador")
    controller.assign_tester("Maria", "Tester")

    view.display_tasks(controller.tasks)
    view.display_engineers(controller.engineers)