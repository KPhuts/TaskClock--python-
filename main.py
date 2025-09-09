from tasks import *
from Clock import *
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from tasks import Task, tasks  # import the classes and the list

class TaskManager(BoxLayout):
    def add_task(self, name):
        new_task = Task(name, priority=1)
        tasks.append(new_task)


    
new_task = tasks.append(task("Sample Task", priority=2))
print(f"Added task: {new_task.name}")



    

