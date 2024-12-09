#This is the MPCS50101 Final Project for Cole Simner
import argparse
import pickle

class Task:
    """Representation of a task
  
    Attributes:
              - created - date
              - completed - date
              - name - string
              - unique id - number
              - priority - int value of 1, 2, or 3; 1 is default
              - due date - date, this is optional
    """
    def __init__(self, name, priority = 1):
        self.created = None #needs to change
        self.completed = None #this is a value that we will pass in
        self.name = name
        self.unique_id = None #needs to change
        self.priority = priority
        self.due_date = None #This is optional
  

class Tasks:
    """A list of 'Task' objects."""
    def __init__(self):
        """Read pickled tasks file into a list."""
        self.tasks = []
        #code here

    def pickle_tasks(self):
        """Pickle your task list to a file"""
        #code here
    
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
    main()