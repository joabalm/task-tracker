
# TASK TRACKER
Task tracker is a project used to track and manage your tasks. In this task, you will build a simple command line interface (CLI) to track what you need to do, what you have done, and what you are currently working on. This project will help you practice your programming skills, including working with the filesystem, handling user inputs, and building a simple CLI application.

## Objetivo 🎯
Practice your habilities with programming logic, python and CLI. 

## Ferramentas 🛠️
[![python](https://img.shields.io/badge/Python-000?style=for-the-badge&logo=python)](https://docs.github.com/)
[![Pycharm](https://img.shields.io/badge/Pycharm-000?style=for-the-badge&logo=Pycharm&logoColor=green)](https://www.jetbrains.com/pt-br/pycharm/) 
[![Git](https://img.shields.io/badge/Git-000?style=for-the-badge&logo=git&logoColor=E94D5F)](https://git-scm.com/doc) 

### Requirement
#### Each task should have the following properties:

- id: A unique identifier for the task
- description: A short description of the task
- status: The status of the task (todo, in-progress, done)
- createdAt: The date and time when the task was created
- updatedAt: The date and time when the task was last updated

#### The list of commands and their usage is given below:

- #### Adding a new task
    - task-cli add "Buy groceries"
    - Output: Task added successfully (ID: 1)

- #### Updating and deleting tasks
    - task-cli update 1 "Buy groceries and cook dinner"
    -  task-cli delete 1

- #### Marking a task as in progress or done
    - task-cli mark-in-progress 1
    - task-cli mark-done 1

- #### Listing all tasks
    - task-cli list

- #### Listing tasks by status
    - task-cli list done
    - task-cli list todo
    - task-cli list in-progress

### Instructions (EN/US)
#### Set Up Your Development Environment
Choose a programming language you are comfortable with (e.g., Python, JavaScript, etc.), in this task will be using the Pyhton.
Ensure you have a code editor or IDE installed (e.g., VSCode, PyCharm), in this task will bw using the Pycharm.
#### Project Initialization
Create a new project directory for your Task Tracker CLI.
Initialize a version control system (e.g., Git) to manage your project.
#### Implementing Features

1. After create your pyhton file, start configuring the libs that you will using, with in the example below.
>
    import argparse
    from datetime import datetime
    import json

2. Create a json file and reference his.
>
    file_path = "data.json"
3. Create the functions for the tasks.
    > 
## Function add new task 
    # Function to add a new task
        def add(description):
    # Load the JSON data from the file
        with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)  # Ensure this is a list

    # If data is not a list, initialize it as a list
        if not isinstance(data, list):
            data = []

    # Determine the new task ID
        last_value = data[-1]["id"] if data else 0
        new_id = last_value + 1

    # Create a new task dictionary
        new_task = {
            "id": new_id,
            "description": description,
            "status": "to do",
            "creatAt": date_time_str,
            "updateAt": ""
        }

    # Append the new task to the list
        data.append(new_task)

    # Save the updated list of tasks back to the file
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    # Return the result
        print(f"Task added successfully (ID:       {new_id})")

# Function to delete the task

        def delete(id_delete):
    # Load the JSON data from the file
        with open(file_path, "r") as file:
        data = json.load(file)  # Ensure this is a list

    # If data is not a list, initialize it as a list
        if not isinstance(data, list):
        data = []

    # Find the index of task list
        for index, task in enumerate(data):
            id_delete = int(id_delete)
            if task.get('id') == id_delete:
                index_delete = index
                break

    # Remove the task and return the result
        if index_delete is not None:
            removed_task = data.pop(index_delete)
            print(f"Task of ID {removed_task['id']} removed successfully.")
        else:
            print(f"Task of ID {id_delete} not found.")

    # Save the updated data back to the file
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

# Function to update the task
        def update(id_update, description):

    # Load the JSON data from the file
        with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)  # Ensure this is a list

    # If data is not a list, initialize it as a list
        if not isinstance(data, list):
            data = []

    # Identify the id and create the update
        update = False
        for index, task in enumerate(data):
            id_update = int(id_update)
            if task.get("id") == id_update:
                task["description"] = description,
                task["updateAt"] = date_time_str
                update = True
                break

    #Return the result
        if update:
            print(f"Task of ID {id_update} updated successfully.")
        else:
            print(f"Task of ID {id_update} not found.")

    # Save the updated list of tasks to the file
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    
# Main function to parse CLI arguments
        def main():
        parser = argparse.ArgumentParser(
            prog="task-manager",
            description="Task Manager CLI",
        )

        subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Subparse for "add" command
        parser_add = subparsers.add_parser("add", help="Add a new task")
        parser_add.add_argument("description", type=str, help="The description of the new task")

    # Subparse for "delete" command
        parser_delete = subparsers.add_parser("delete", help="Delete a task")
        parser_delete.add_argument("id_delete",type=str, help="task id to be deleted")

    # Subparse for "update" command
        parser_update = subparsers.add_parser("update", help="Update the task")
        parser_update.add_argument("id_update", type=str, help="task id to be updated")
        parser_update.add_argument("description", type=str, help="task description to be updated")

    # Parse the arguments
        args = parser.parse_args()

    # Execute the appropriate function based on the subcommand
        if args.command == "add":
            add(args.description)
        elif args.command == "delete":
            delete(args.id_delete)
        elif args.command == "update":
            update(args.id_update,args.description)
        else:
            parser.print_help()

        if __name__ == "__main__":
            main()
    




