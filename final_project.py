#This is the MPCS50101 Final Project for Cole Simner
import argparse
import argparse
import pickle
from datetime import datetime
import sys
import random
import string
import re

class Task:
    """Representation of a task
  
    Attributes:
              - created - date, displayed as MM/DD/YYYY
              - raw_created - datetime, the datetime stamp when a task was created
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
            print("There was an error with creating your task. Run 'todo -h' for usage instructions")
            sys.exit(1)
        self.created = self.__create_date()
        self.raw_created = self.__raw_create_date()
        self.completed = self.__validate_completed(completed) #This sets the default to None since the user won't set it right away, it performs error handling if there is a input passed
        self.unique_id = self.__create_unique_id()
        self.priority = self.__validate_priority(priority)
        self.due_date = self.__validate_due_date(due_date) #This sets the optional value of due date to None and performs error handling when a value is passed

    def __str__(self):
        """Return a string representation of the Task object."""
        return f"Task ID: {self.unique_id}, Name: '{self.name}', Due: {self.due_date}, Priority: {self.priority}, Created: {self.created}, Completed: {self.completed}"
    
    def __create_date(self):
        """This is a private method used to create the date value for the 'created' attribute. It returns a string."""
        current = datetime.now()

        formatted_date = current.strftime("%m/%d/%Y")

        return formatted_date
    
    def __raw_create_date(self):
        """This is a private method used to create the raw date value for a special attribute uses to sort dates. It returns a string."""
        current = datetime.now()

        formatted_time = current.strftime('%a %b %d %H:%M:%S CST %Y')

        return formatted_time
    
    def __create_unique_id(self):
        """This is a private method used to create the unique ID attribute for a Task. It generates 3 random numbers and 2 random letters and returns the concatenated string."""
        #this generates 73 billion possible combinations
        random_digits = ''.join(random.choices(string.digits, k=4)) #generate three random numbers
        random_letter = ''.join(random.choices(string.ascii_letters, k=4)) #generate 3 random letters
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
        name_check = name.strip()
        if len(name_check) == 0:
            return None
        elif not re.search(r'[a-zA-Z]', name_check):
            return None
        elif len(name_check) > 25:
            name_check = name_check[:25]
            return name_check
        else:
            return name.strip()
        
    def __validate_completed(self, completed):
        """This is a private method used to validate the completed attribute or set the default value to None. It returns either a formatted date or None."""
        if completed is None:
            return None
        else:
            if self.__validate_date(completed):
                return completed
            else:
                print(f"You did not enter a correct date in MM/DD/YYYY format.") #When an error occurs, defaut the value back to None and display a message
                return None 
            
    def __validate_due_date(self, due_date):
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
    
    def add_tasks(self, name, priority=1, due_date= None):
        """This method is used to create a task, it inherets functionality from the Task class and returns the  """
        task = Task(name, priority, due_date)
        return task
    
    def display_list(self):
        """This method is used for the list operation. """
        incomplete_tasks = []
        for task in self.tasks:
            if task.completed is None:
                current_date = datetime.now()
                created_date = datetime.strptime(task.created, "%m/%d/%Y")
                age = (current_date - created_date).days
                task.age = age
                incomplete_tasks.append(task)
        
        sorted_incomplete_tasks = sorted(incomplete_tasks, 
                                         key=lambda task: (datetime.strptime(task.due_date, "%m/%d/%Y") if task.due_date 
                                                           else datetime.max, task.priority))
        return sorted_incomplete_tasks
    
    def list_query(self, search):
        """This is a docstring for the query method"""
        task_word_sets = []

        for task in self.tasks:  # Loop over all tasks (N tasks)
            if task.completed is None:
            # Remove punctuation from task name and split by space
                task_name_cleaned = re.sub(r"[^\w\s]", "", task.name.lower())  # Removes punctuation
                task_words = set(task_name_cleaned.split())  # Split into words and make a set
                task_word_sets.append((task, task_words))
    
        matching_tasks = []
        query_terms = set(term.lower() for term in search)  # Preprocess query terms (O(M))

        # Check for matches (substring match)
        for task, task_words in task_word_sets:  # Loop over all tasks (N tasks)
            if any(any(term in word for term in query_terms) for word in task_words):  # Check for substring match
               matching_tasks.append(task)
        
        final_tasks = []
        for task in matching_tasks:
            current_date = datetime.now()
            created_date = datetime.strptime(task.created, "%m/%d/%Y")
            age = (current_date - created_date).days
            task.age = age
            final_tasks.append(task)
        
        return final_tasks
    
    def list_done(self, task_id):
        """This is a docstring for the done functionality that updates the 'completed' field of a task."""
        for task in self.tasks:
            if task.unique_id == task_id:
                current_date = datetime.now()
                formatted_date = current_date.strftime("%m/%d/%Y")
                raw_time = current_date.strftime('%a %b %d %H:%M:%S CST %Y')
                task.completed = formatted_date
                task.raw_completed = raw_time
                self.pickle_tasks()
                return True
        else:
            return False
        
                
    
    def list_delete(self, task_id):
        """This is a docstring for the delete functionality that deletes task."""
        for task in self.tasks:
            if task.unique_id == task_id:
                self.tasks.remove(task)
                self.pickle_tasks()
                return True
        else:
            return False
        
    
    def list_report(self):
        """This is a docstring for the Task report command"""
        all_tasks = []
        for task in self.tasks:
                current_date = datetime.now()
                created_date = datetime.strptime(task.created, "%m/%d/%Y")
                age = (current_date - created_date).days
                task.age = age
                all_tasks.append(task)
        
        sorted_tasks = sorted(all_tasks, key=lambda task: task.priority)
        
        return sorted_tasks


def main():
    """ All the real work driving the program!"""
    parser = argparse.ArgumentParser(description= "update the task list.")
    parser.add_argument('--add', type= str, required= False, help= "add one task to your list by passing in an alphanumeric name.")
    parser.add_argument('--list', action='store_true', required=False, help="list all tasks that have not been completed, by due date then priority.")
    parser.add_argument('--report', action='store_true', required=False, help="list all tasks that have not been completed, by due date then priority.")
    parser.add_argument('--done', type= str, required= False, help= "the unique ID of the task you want to mark 'complete.'")
    parser.add_argument('--delete', type= str, required= False, help= "the unique ID of the task you want to remove from the list.")
    parser.add_argument('--query', type=str, required=False, nargs="+", help="input a series of string-search to find key terms in task names")
    parser.add_argument('--due', type=str, required=False, help="the due date in MM/DD/YYYY format.")
    parser.add_argument('--priority', type= int, required=False, default=1, help="the priority of a task; the default is 1")



    args = parser.parse_args()

    task_list = Tasks()
    
    #for task in task_list.tasks:
    #    print(task)

    if args.add:
        new_task = task_list.add_tasks(name=args.add, priority=args.priority, due_date=args.due)
        task_list.tasks.append(new_task)
        print(f"Created task {new_task.unique_id}")
        task_list.pickle_tasks()
        return
    
    elif args.list:
        sorted_incomplete_tasks = task_list.display_list()
        print(f"{'ID':<10} {'Age':<5} {'Due Date':<12} {'Priority':<10} {'Task':<25}")
        print(f"{'-' * 8}   {'-' * 3}   {'-' * 10}   {'-' * 8}   {'-' * 4}")
        
        for task in sorted_incomplete_tasks:
            age_str = f"{task.age}d" if task.age is not None else "0d"
            due_date_str = task.due_date if task.due_date else "-"
            print(f"{task.unique_id:<10} {age_str:<5} {due_date_str:<12}  {task.priority:<9} {task.name:<25}")
        return
    
    elif args.report:
        all_tasks_debugging = task_list.list_report()
        
        print(f"{'ID':<10} {'Age':<5} {'Due Date':<12} {'Priority':<10} {'Task':<25}    {'Created':<30} {'Completed':<30}")
        print(f"{'-' * 8}   {'-' * 3}   {'-' * 10}   {'-' * 8}   {'-' * 4}                         {'-' * 27}    {'-' * 27}")
    
        for task in all_tasks_debugging:
            # Format age, due date, and completed date with fallback values
            age_str = f"{task.age}d" if task.age is not None else "0d"
            due_date_str = task.due_date if task.due_date else "-"
            completed_str = task.raw_completed if hasattr(task, 'raw_completed') else "-"
        
            # Print task details with aligned columns
            print(f"{task.unique_id:<10} {age_str:<5} {due_date_str:<12}  {task.priority:<9} {task.name:<25}    {task.raw_created:<30} {completed_str:<30}")
        return
    
    elif args.done:
        successfully_updated = task_list.list_done(args.done)
        if successfully_updated == True:
            print(f"Completed task ID {args.done}")
            return
        else:
            print(f"Could not identity task ID {args.done}")
            return
    
    elif args.delete:
        successfully_deleted = task_list.list_delete(args.delete)
        if successfully_deleted == True:
            print(f"Deleted task ID {args.delete}")  
            return
        else:
            print(f"Could not identify task ID {args.delete}")
            return
    
    elif args.query: #I made a runtime tradeoff here with the justification of better search performance for worse runtime O(N^3) vs O(N)
        final_tasks = task_list.list_query(args.query)
        
        print(f"{'ID':<10} {'Age':<5} {'Due Date':<8}  {'Priority':<10}  {'Task':<1}")
        print(f"{'-' * 8}   {'-' * 3}\t{'-' * 10} {'-' * 8}    {'-' * 5}")
        
        for task in final_tasks:
            age_str = f"{task.age}d" if task.age is not None else "0d"
            due_date_str = task.due_date if task.due_date else "-"
            #print(f"{task.unique_id}\t{age_str}\t{task.due_date}\t{task.priority}\t{task.name}")
            print(f"{task.unique_id:<10} {age_str:<5} {due_date_str:<12} {task.priority:<8} {task.name:<1}")
        return


    else:
        print("You did not call a valid operation, try -h for a list of valid operations")

if __name__ == "__main__":
    main()