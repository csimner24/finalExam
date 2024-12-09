#This is the MPCS50101 Final Project for Cole Simner
import argparse
import pickle
from datetime import datetime
import pickle
import task_module as t

cole = t.Task("cole", priority=3)



class Tasks:
    """A list of 'Task' objects."""
    def __init__(self, pickle_file=".todo.pickle"):
        """Read pickled tasks file into a list."""
        self.tasks = []
        self.pickle_file = pickle_file
        self.tasks = self.pickle_read()
    
    def pickle_read(self):
        """Read from the pickle file to getr a list of tasks."""
        try:
            # Try to open the pickle file in read-binary mode
            with open(self.pickle_file, "rb") as file:
                # Load the list of tasks from the pickle file
                self.tasks = pickle.load(file)
        except FileNotFoundError:
            print(f"The task list does not exist, the list of tasks is empty.")
            return self.tasks
        except Exception as e:
            print(f"Error while loading tasks: {e}")
            return self.tasks

    def pickle_tasks(self):
        """Pickle your task list to a file"""
        try:
            # Open the pickle file in write-binary mode
            with open(self.pickle_file, "wb") as file:
                pickle.dump(self.tasks, file)
        except Exception as e:
            # Handle any exception that occurs during saving
            print(f"Error while saving tasks: {e}")
    
    ### add, list, report, done, delete, etc. functionality ###

def main():
    """ All the real work driving the program!"""
    parser = argparse.ArgumentParser(description= "update the task list.")
    parser.add_argument('--add', type= str, required= False, help= "a task string to add to your list")
    parser.add_argument('--priority', type= int, required=False, default=1, help="priority of a task; the default is 1")

    args = parser.parse_args()

    task_list = Tasks()

    if args.add:
        print(f"Add {args.add} to our last of todo's with priority {args.priority}.")
        task_list.add(args.add, args.priority)

    elif args.report:
        print("Printing out the report")
    pass

    task_list.pickle_tasks()
    exit()



if __name__ == "__main__":
    cole = Tasks()
    print(cole)
    print(cole.tasks)
    steve = cole.tasks
    jeff = len(steve)
    print(jeff)