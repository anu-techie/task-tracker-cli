'''Task CLI Application'''
# native file system module to interact with the JSON file.

import sys
from task.core import (add_task, update_task, delete_task, change_status, list_tasks, print_help)

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







