#This is the MPCS50101 Final Project for Cole Simner
import argparse
import pickle
from datetime import datetime

class Task:
    """Representation of a task
  
    Attributes:
              - created - date
              - completed - date
              - name - string
              - unique id - number
              - priority - int value of 1, 2, or 3; 1 is default
              - due date - date, this is optional and defaults to None
    """
    _new_id = 0
    def __init__(self, name, priority= 1, due_date= None, completed= None):
        self.created = self.__create_date()
        self.completed = self.__validate_completed(completed) #This sets the default to None since the user won't set it right away, it performs error handling if there is a input passed
        self.name = name
        self.name = self.__validate_name(name)
        self.unique_id = self.__create_unique_id()
        self.priority = self.__validate_priority(priority)
        self.due_date = self.__validate_due_date(due_date) #This sets the optional value of due date to None and performs error handling when a value is passed

    def __create_date(self):
        """This is a private method used to create the date value for the 'created' attribute. It returns a string."""
        current = datetime.now()

        formatted_date = current.strftime("%m/%d/%Y")

        return formatted_date
    
    def __create_unique_id(self):
        """This is a private method used to create the unique ID attribute for a Task. It returns an integer."""
        Task._new_id += 1
        return Task._new_id
    
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
        if len(name_check) == 0:
            print("You cannot enter a blank name, the name value will therefore be set to None.")
            return None
        else:
            return name.strip()
        
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