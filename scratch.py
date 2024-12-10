import argparse
import pickle
from datetime import datetime
import sys


parser = argparse.ArgumentParser(description= "update the task list.")

parser.add_argument('--add', type= str, required= False, help= "a task string to add to your list")
parser.add_argument('--due', type=str, required=False, help="due date in DD/MM/YYYY format")
parser.add_argument('--priority', type= int, required=False, default=1, help="priority of a task; the default is 1")
parser.add_argument('--query', type=str, required=False, nargs="+", help="search for key terms in task names")
parser.add_argument('--list', action='store_true', required=False, help="list all tasks that have not been completed")

args = parser.parse_args()

import random
import string

def __create_unique_id():
    """This is a private method used to create the unique ID attribute for a Task.
    It returns a string of 3 random digits followed by 1 random lowercase letter."""
    
    # Generate 3 random digits (0-9)
    random_digits = ''.join(random.choices(string.digits, k=3))
    
    # Generate 1 random lowercase letter (a-z)
    random_letter = ''.join(random.choices(string.ascii_uppercase, k=2))
    
    # Concatenate the digits and the letter to create the unique ID
    unique_id = random_digits + random_letter
    
    return unique_id

cole = __create_unique_id()
print(cole)



