#This is the MPCS50101 Final Project for Cole Simner
import argparse
import argparse
import pickle
from datetime import datetime
import sys
import random
import string

class Task:
    """Representation of a task
  
    Attributes:
              - created - date
              - completed - date, this is optionally defined as MM/DD/YYYY
              - name - string
              - unique id - number, this is created automatically
              - priority - int value of 1, 2, or 3; 1 is default
              - due date - date, this is optional and defaults to None
    """
    def __init__(self, name, priority= 1, due_date= None, completed= None):
        self.name = name
        self.name = self.__validate_name(name)
        if self.name is None:
            print("There was an error in creating your task. Run 'todo -h' for usage instructions")
            sys.exit(1)
        self.created = self.__create_date()
        self.raw_created = self.__raw_create_date()
        self.completed = self.__validate_completed(completed) #This sets the default to None since the user won't set it right away, it performs error handling if there is a input passed
        self.unique_id = self.__create_unique_id()
        self.priority = self.__validate_priority(priority)
        self.due_date = self.__validate_due_date(due_date) #This sets the optional value of due date to None and performs error handling when a value is passed

    def __str__(self):
        """Return a string representation of the Task object."""
        return f"Task ID: {self.unique_id}, Name: '{self.name}', Due: {self.due_date}, Priority: {self.priority}, Created: {self.created}"
    
    def __create_date(self):
        """This is a private method used to create the date value for the 'created' attribute. It returns a string."""
        current = datetime.now()

        formatted_date = current.strftime("%m/%d/%Y")

        return formatted_date
    
    def __raw_create_date(self):
        """This is a private method used to create the raw date value for a special attribute uses to sort dates. It returns a string."""
        current = datetime.now()

        return current
    
    def __create_unique_id(self):
        """This is a private method used to create the unique ID attribute for a Task. It generates 3 random numbers and 2 random letters and returns the concatenated string."""
        #this generates 17 million possible combinations
        random_digits = ''.join(random.choices(string.digits, k=3)) #generate three random numbers
        random_letter = ''.join(random.choices(string.ascii_uppercase, k=3)) #generate 3 random letters
        unique_id = random_digits + random_letter
        return unique_id
    
    def __validate_date(self, date_value):
        """This is a private method to validate if a date string is in MM/DD/YYYY format."""
        try:
            datetime.strptime(date_value, "%m/%d/%Y")
            return True
        except:
            return False
        
    def __validate_name(self, name):
        """This is a private method used to validate the name attribute or set the default value to None. It returns either a string name or None."""
        name_check = name.replace(" ", "").strip()
        try:
            float(name_check)
            return None
        except:
            pass
        if len(name_check) == 0:
            return None
        else:
            return name.lower().strip()
        
    def __validate_completed(self, completed=None):
        """This is a private method used to validate the completed attribute or set the default value to None. It returns either a formatted date or None."""
        if completed is None:
            return None
        else:
            if self.__validate_date(completed):
                return completed
            else:
                print(f"You did not enter a correct date in MM/DD/YYYY format.") #When an error occurs, defaut the value back to None and display a message
                return None 
            
    def __validate_due_date(self, due_date=None):
        """This is a private method used to validate the completed attribute or set the default value to None. It returns either a formatted date or None."""
        if due_date is None:
            return None
        else:
            if self.__validate_date(due_date):
                return due_date
            else:
                print("You did not enter a correct date in MM/DD/YYYY format.")
                return None #When an error occurs, defaut the value back to None and display a message
    
    def __validate_priority(self, priority):
        """This is a private method used to validate the priority attribute or set the default value to 1. It returns the integers 1, 2, or 3."""
        if priority == 1:
            return 1
        elif priority == 2:
            return 2
        elif priority == 3:
            return 3
        else:
            print("Please enter priority as an integer of either 1, 2, or 3. The default is 1.")
            return 1


class Tasks:
    """A list of 'Task' objects."""
    def __init__(self, pickle_file=".todo.pickle"):
        """Read pickled tasks file into a list."""
        self.tasks = []
        self.pickle_file = pickle_file
        self.tasks = self.pickle_read()
    
    def pickle_read(self):
        """Read existing tasks from a pickle file if applicable."""
        try:
            with open(self.pickle_file, "rb") as file:
                self.tasks = pickle.load(file)
        except FileNotFoundError:
            self.tasks = []
        except Exception as e:
            print(f"Error while loading tasks: {e}")
        return self.tasks

    def pickle_tasks(self):
        """Write the list objects to a pickle file"""
        try:
            with open(self.pickle_file, "wb") as file:
                pickle.dump(self.tasks, file)
        except Exception as e:
            print(f"Error while saving tasks: {e}")
    
    ### add, list, report, done, delete, etc. functionality ###

def main():
    """ All the real work driving the program!"""
    parser = argparse.ArgumentParser(description= "update the task list.")
    parser.add_argument('--add', type= str, required= False, help= "add a task to your list by passing in an alphanumeric name")
    parser.add_argument('--done', type= str, required= False, help= "the date completed in MM/DD/YYYY format")
    parser.add_argument('--due', type=str, required=False, help="the due date in MM/DD/YYYY format")
    parser.add_argument('--priority', type= int, required=False, default=1, help="the priority of a task; the default is 1")
    parser.add_argument('--query', type=int, required=False, nargs="+", help="input a series of string-search to find key terms in task names")
    parser.add_argument('--list', action='store_true', required=False, help="list all tasks that have not been completed")


    args = parser.parse_args()

    task_list = Tasks()

    if args.add:
        new_task = Task(name=args.add, priority=args.priority, due_date=args.due, completed=args.done)
        task_list.tasks.append(new_task)
        print(f"Created task {new_task.unique_id}")
        task_list.pickle_tasks()

    #for task in task_list.tasks:
    #    print(task)
    
    exit()
    




if __name__ == "__main__":
    main()