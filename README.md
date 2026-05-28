````markdown
# Task Tracker CLI

A simple command-line task tracker built with Python.

This project allows users to add, update, delete, mark, and list tasks using terminal commands. Tasks are stored locally in a JSON file.

## Project Description

Task Tracker CLI is a beginner-friendly command-line application for managing tasks. It helps users keep track of what they need to do, what they are currently working on, and what they have completed.

The main goal of this project is to practice working with:

- Command-line arguments
- File handling
- JSON data storage
- Basic CRUD operations
- Error handling
- Git and GitHub project workflow

## Features

- Add a new task
- Update an existing task
- Delete a task
- Mark a task as in progress
- Mark a task as done
- List all tasks
- List tasks by status:
  - todo
  - in-progress
  - done
- Store tasks in a local JSON file
- Automatically create the JSON file if it does not exist
- Handle invalid commands and errors gracefully

## Technologies Used

- Python 3
- JSON
- Native Python file system modules
- Git
- GitHub

## Project Structure

```bash
task-tracker-cli/
│
├── task_cli.py
├── README.md
├── .gitignore
└── tasks.example.json
```

## Task Properties

Each task contains the following properties:

| Property | Description |
|---|---|
| id | A unique ID for each task |
| description | The task description |
| status | The current status of the task |
| createdAt | The date and time when the task was created |
| updatedAt | The date and time when the task was last updated |

Example task object:

```json
{
  "id": 1,
  "description": "Buy groceries",
  "status": "todo",
  "createdAt": "2026-05-28T10:00:00",
  "updatedAt": "2026-05-28T10:00:00"
}
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/task-tracker-cli.git
```

Move into the project directory:

```bash
cd task-tracker-cli
```

Make sure Python is installed:

```bash
python --version
```

or:

```bash
python3 --version
```

## Usage

### Add a new task

```bash
python task_cli.py add "Buy groceries"
```

Example output:

```bash
Task added successfully (ID: 1)
```

### List all tasks

```bash
python task_cli.py list
```

### List tasks by status

List completed tasks:

```bash
python task_cli.py list done
```

List tasks that are not done yet:

```bash
python task_cli.py list todo
```

List tasks currently in progress:

```bash
python task_cli.py list in-progress
```

### Update a task

```bash
python task_cli.py update 1 "Buy groceries and cook dinner"
```

### Delete a task

```bash
python task_cli.py delete 1
```

### Mark a task as in progress

```bash
python task_cli.py mark-in-progress 1
```

### Mark a task as done

```bash
python task_cli.py mark-done 1
```

## Example Workflow

```bash
python task_cli.py add "Learn Python file handling"
python task_cli.py add "Build a CLI project"
python task_cli.py list
python task_cli.py mark-in-progress 1
python task_cli.py mark-done 1
python task_cli.py update 2 "Build and publish a CLI project"
python task_cli.py list done
python task_cli.py delete 2
```

## Data Storage

All tasks are stored in a file called:

```bash
tasks.json
```

This file is created automatically in the current directory when tasks are added.

Example `tasks.json`:

```json
[
  {
    "id": 1,
    "description": "Learn Python",
    "status": "todo",
    "createdAt": "2026-05-28T10:00:00",
    "updatedAt": "2026-05-28T10:00:00"
  }
]
```

## Error Handling

The application handles common errors such as:

- Missing task description
- Invalid task ID
- Updating a task that does not exist
- Deleting a task that does not exist
- Invalid status filters
- Unknown commands
- Empty or missing JSON file

## Git Ignore

The `tasks.json` file should be added to `.gitignore` because it contains local user data.

Example `.gitignore`:

```gitignore
__pycache__/
*.pyc
tasks.json
```

A sample file named `tasks.example.json` can be included to show the expected JSON structure.

## Future Improvements

Some possible improvements for this project:

- Add task priorities
- Add due dates
- Add search functionality
- Add task categories
- Improve terminal output formatting
- Add color-coded task statuses
- Add unit tests
- Package the app as a real CLI command

## Project URL

This project is based on the Task Tracker project from roadmap.sh:

https://roadmap.sh/projects/task-tracker