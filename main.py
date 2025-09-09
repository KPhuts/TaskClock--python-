from tasks import *
from Clock import *
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from tasks import Task, tasks

class TaskScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        # Input field
        self.input = TextInput(hint_text="Enter task name", size_hint_y=None, height=40)
        self.add_widget(self.input)

        # Add button
        self.add_button = Button(text="Add Task", size_hint_y=None, height=40)
        self.add_button.bind(on_press=self.add_task)
        self.add_widget(self.add_button)

        # Scrollable area for tasks
        self.scroll = ScrollView()
        self.task_list = BoxLayout(orientation='vertical', size_hint_y=None)
        self.task_list.bind(minimum_height=self.task_list.setter('height'))
        self.scroll.add_widget(self.task_list)
        self.add_widget(self.scroll)

    def add_task(self, instance):
        name = self.input.text.strip()
        if name:
            new_task = Task(name, priority=1)
            tasks.append(new_task)
            self.task_list.add_widget(Label(text=f"{new_task.name} (Priority {new_task.priority})"))
            self.input.text = ""

class TaskApp(App):
    def build(self):
        return TaskScreen()

if __name__ == "__main__":
    TaskApp().run()


