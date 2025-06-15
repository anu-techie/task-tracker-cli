import os
import json
from datetime import datetime

DATA_DIR = 'data'
TASK_FILE = os.path.join(DATA_DIR, 'tasks.json')

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def load_task():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, 'r') as file:
        return json.load(file)
    
def save_task(tasks):
    # JSON file will be created automatically if it does not exist.
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_new_id(tasks):
    return max([t['id'] for t in tasks], default=0)+1
