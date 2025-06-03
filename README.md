# Task Tracker CLI App

A simple command-line task management tool built in Python.  
Manage your to-do list right from your terminal — add, update, delete, change status, and list tasks!

---

## Features

- Add new tasks with descriptions  
- Update existing tasks by ID  
- Delete tasks by ID  
- Change task status (`todo`, `in-progress`, `done`)  
- List all tasks or filter by status  
- Tasks saved persistently in a JSON file (`tasks.json`)  

---

## Installation

Follow these steps to get your Task Tracker CLI up and running:

1. **Download or clone the repository**

   - To download - as a ZIP, click the **Code** button and select **Download ZIP**.  
   - Or clone via Git (if you have Git installed):  
     ```bash
     git clone <repository-url>
     ```
   Replace `<repository-url>` with your actual GitHub repository link.

2. **Navigate to the project directory**

   ```bash
   cd <project-folder>
   ```
3. **Ensure you have Python 3 installed**

    ```bash
   python --version
   ```
   If Python is not installed, download it from python.org.

4. **Run the Task Tracker CLI**
    ```bash
    python task-cli.py help
    ```
    to see available commands and usage instructions.
---

## Data Storage
Tasks are saved in tasks.json located in the same directory as the script. This file is created automatically when you add your first task.

---

## Acknowledgments

This project was inspired by and developed following the excellent guidance from [roadmap.sh](https://roadmap.sh). Special thanks to their clear tutorials and project ideas.

---

## Project URL

For detailed project guidelines and ideas, visit:
[https://roadmap.sh/projects/task-tracker](https://roadmap.sh/projects/task-tracker)