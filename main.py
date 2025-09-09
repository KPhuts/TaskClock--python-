from tasks import *
from Clock import *



from kivy.app import App

def main():
    task_manager = TaskManager()
    clock = Clock(task_manager)
    clock.run()

if __name__ == "__main__":
    main()


    

