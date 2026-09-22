from task import Task

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name):
        task = Task(name)
        self.tasks.append(task)

    def complete_task(self, number):
        if 0 <= number < len(self.tasks):
            self.tasks[number].complete()

    def remove_task(self, number):
        if 0 <= number < len(self.tasks):
            self.tasks.pop(number)

    def show_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks.")
        else:
            for i in range(len(self.tasks)):
                print(i + 1, self.tasks[i])