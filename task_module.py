# This file stores the Task class code
import argparse
import pickle
from datetime import datetime
import sys

class Task:
    """Representation of a task
  
    Attributes:
              - created - date
              - raw_created - a datetime value used for the organization of tasks, not for user manipulation
              - completed - date
              - name - string
              - unique id - number
              - priority - int value of 1, 2, or 3; 1 is default
              - due date - date, this is optional and defaults to None
    """
    _new_id = 0
    def __init__(self, name, priority= 1, due_date= None, completed= None):
        self.name = name
        self.name = self.__validate_name(name)
        if self.name is None:
            print("The task name you provided was invalid, you must provide a non blank name.")
            sys.exit(1)
        self.created = self.__create_date()
        self.raw_created = self.__raw_create_date()
        self.completed = self.__validate_completed(completed) #This sets the default to None since the user won't set it right away, it performs error handling if there is a input passed
        self.unique_id = self.__create_unique_id()
        self.priority = self.__validate_priority(priority)
        self.due_date = self.__validate_due_date(due_date) #This sets the optional value of due date to None and performs error handling when a value is passed

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


if __name__ == "__main__":
    task1 = Task("1 ")
    print(f"Task Name: {task1.name}, Created: {task1.created}, Unique ID: {task1.unique_id}, Priority: {task1.priority}, Completed: {task1.completed}, Due Date: {task1.due_date}")

    #current = datetime.now()
    #print(current)
    #print(type(current))