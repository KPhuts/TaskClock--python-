

class task:
    def __init__(self, name, priority, description="No description provided", estimated_minutes=0):
        self.name = name
        self.priority = priority
        self.description = description
        self.estimated_minutes = estimated_minutes

    def update_priority(self, new_priority):
        self.priority = new_priority

    def update_description(self, new_description):
        self.description = new_description
    
    def update_estimated_time(self, new_time):
        self.estimated_time = new_time
 
    def display(self):
        print(f"Task: {self.name}, Priority: {self.priority}")
    

    


class substask(task):
    def __init__(self, name, priority, parent_task):
        super().__init__(name, priority)
        self.parent_task = parent_task

    def display(self):
        print(f"Subtask: {self.name}, Priority: {self.priority}, Parent Task: {self.parent_task.name}")


def create_task(name, priority):
    return task(name, priority)

def create_subtask(name, priority, parent_task):
    return substask(name, priority, parent_task)
