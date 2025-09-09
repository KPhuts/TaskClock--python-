from tasks import *
from Clock import *
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from tasks import Task, tasks

class TaskScreen(BoxLayout):
    def add_task(self, task_name):
        from kivy.uix.label import Label
        if task_name.strip():
            new_task = Task(task_name, priority=1)
            tasks.append(new_task)
            self.ids.task_list.add_widget(Label(text=f"{new_task.name} (Priority {new_task.priority})"))

class TaskApp(App):
    def build(self):
        return TaskScreen()

if __name__ == "__main__":
    TaskApp().run()


