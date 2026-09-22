class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False

    def complete(self):
        self.completed = True

    def __str__(self):
        if self.completed:
            return "[Done] " + self.name
        else:
            return "[ ] " + self.name
