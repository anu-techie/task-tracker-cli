from .utils import (load_task, save_task, get_current_time, get_new_id)

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