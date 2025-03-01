import csv
import random

def load_problems(file_path):
    '''Load Problems from CSV file.'''
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        problems = list(reader)
        return problems
    
    
def get_random_problem(problems, difficulty):
    '''Get a random problem of the specified difficulty.'''
    filtered = [p for p in problems if p['Difficulty'].lower() == difficulty.lower()]
    return random.choice(filtered) if filtered else None