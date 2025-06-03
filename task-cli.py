'''Task CLI Application'''
# native file system module to interact with the JSON file.
import os
import sys
import json
from datetime import datetime

task_file = 'tasks.json'

def load_task():
    if not os.path.exists(task_file):
        return []
    with open(task_file, 'r') as file:
        return json.load(file)
    
def save_task(tasks):
    # JSON file will be created automatically if it does not exist.
    with open(task_file, 'w') as file:
        json.dump(tasks, file, indent=4)

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_new_id(tasks):
    return max([t['id'] for t in tasks], default=0)+1

def add_task(description):
    tasks = load_task()
    now = get_current_time()
    task = {
        'id':get_new_id(tasks),
        'description': description,
        'status': 'todo',
        'createdAt': now,
        'updatedAt':now
    }
    tasks.append(task)
    save_task(tasks)
    print(f' Task added : {description}')

def update_task(id, description):
    tasks = load_task()
    for task in tasks:
        if task['id'] == id:
            task['description'] = description
            task['updatedAt'] = get_current_time()
            save_task(tasks)
            print(f'Task{id} updated')
            return
    print('Task not found')

def delete_task(id):
    tasks = load_task()
    tasks = [task for task in tasks if task['id']!=id]
    save_task(tasks)
    print(f'Task {id} deleted')

def change_status(id, status):
    s = ['todo', 'in-progress', 'done']
    if status not in s:
        print('Invalid status')
        return
    
    tasks = load_task()
    for task in tasks:
        if task['id']==id:
            task['status']=status
            task['updatedAt']=get_current_time()
            save_task(tasks)
            print(f'Task {id} status updated successfully')
            return
    print('Task not found')

def list_tasks(status=None):
    tasks = load_task()
    filter_task = tasks if status is None else [task for task in tasks if task['status']==status]
    if not filter_task:
        print('No tasks found')
        return
    for task in filter_task:
        print(f'{task['id']}. {task['description']} | {task['status']} | {task['createdAt']} | {task['updatedAt']}')
    

def print_help():
    print("""
📝 Task CLI - Command Line To-Do App

Available Commands:
  help
      ➤ Show this help message

  add <description>
      ➤ Add a new task
      Example: python task_cli.py add Buy groceries

  update <id> <new description>
      ➤ Update task description
      Example: python task_cli.py update 2 Buy eggs

  delete <id>
      ➤ Delete a task
      Example: python task_cli.py delete 3

  status <id> <status>
      ➤ Change task status (todo | in-progress | done)
      Example: python task_cli.py status 2 done

  list [status]
      ➤ List all tasks or filter by status
      Example: python task_cli.py list
               python task_cli.py list done
""")

# CLI Structure
def main():
    if len(sys.argv) < 2:
        print("Please enter a command or type 'python <filename.py> help' to see available commands.")
        return
    # positional arguments sys.argv[]
    command = sys.argv[1]

    if command == 'help':
        print_help()
    
    elif command == 'add':
        description = ' '.join(sys.argv[2:])
        add_task(description)

    elif command =='update':
        id = int(sys.argv[2])
        description = ' '.join(sys.argv[3:])
        update_task(id, description)

    elif command == 'delete':
        delete_task(int(sys.argv[2]))

    elif command == 'status':
        change_status(int(sys.argv[2]), sys.argv[3])

    elif command == 'list':
        if len(sys.argv)==3:
            list_tasks(sys.argv[2])
        else:
            list_tasks()
    else:
        print('Unknown command')
        print("wanna help then type 'python <filename.py> help' to see available commands.")
    
if __name__ == "__main__":
     main()
