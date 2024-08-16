
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

## Add new task 
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
    
# Function to update the task status to in-progress
    def mark_in_progess(id_update_status):
    
        # Load the JSON data from the file
        with open(file_path, "r",encoding="utf-8") as file:
            data = json.load(file)
    
        # If data is not a list, initialize it as a list
        if not isinstance(data, list):
            data = []
    
        # Update the status of the task
        update = False
        for index, task in enumerate(data):
            id_update_status = int(id_update_status)
            if task.get("id") == id_update_status:
                task["status"] = "in-progress";
                task["updateAt"] = date_time_str
                update = True
                break
        # Return the result
        if update:
            print(f"The task with ID {id_update_status} was updated successfully")
        else:
            print(f"The task with ID {id_update_status} is not found")
    
        # Save the updatd list of tasks from the file
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


# Funcion mark-done
    def mark_done(id_update_task):

        # Load the JSON data from the file
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    
        # If data is not a list, initialize it as a list
        if not isinstance(data, list):
            data = []
    
        # Updated the task status and task updateAt
        update = False
        for index, task in enumerate(data):
            id_update_task = int(id_update_task)
            if task.get("id") == id_update_task:
                task["status"] = "done";
                task["updateAt"] = date_time_str
                update = True
                break
        # Return the result
        if update:
            print("The task with ID {}, is done".format(id_update_task))
        else:
            print("The task with ID {}, is not found".format(id_update_task))
    
        # Save the updatd list of tasks from the file
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

# Function list tasks
    def list_tasks():

        # Load the JSON data from the file
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    
        # Create a dataframe for viewer the results
        df = pd.DataFrame(data)
        print(df)

# Function list tasks where status is done
    def list_done():

        # Load the JSON data from the file
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    
        # Tracker the tasks where status id done and create a dataframe
        result = [d for d in data if d['status'] == "done"]
        df = pd.DataFrame(result)
    
        # Print the result
        print(df)

# Function to list tasks with the status 'to do'
    def list_todo():
    
        # Load the JSON data from the file
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    
        # Filter tasks with status 'to do' and create a dataframe
        result = [d for d in data if d['status'] == "to do"]
        df = pd.DataFrame(result)
        print(df)

# Function to list tasks with the status 'in-progress'
    def list_in_progress():
    
        # Load the JSON data from the file
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    
        # Filter tasks with status 'in-progress' and create a dataframe
        result = [d for d in data if d['status'] == "in-progress"]
        df = pd.DataFrame(result)
        print(df)

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
    
        # Subparser for "mark-in-progress"
        parser_mark_in_progress = subparsers.add_parser("mark_in_progress", help="Updated the task status")
        parser_mark_in_progress.add_argument("id_update_status", type=str, help="task id to be updated")
    
        # Subparser for "mark-done" command
        parser_update_done = subparsers.add_parser("mark_done", help="Update the status with is done")
        parser_update_done.add_argument("id_update_task", type=str, help="Task id for update with is done")
    
        # Subparser for "list" command
        parser_list_tasks = subparsers.add_parser("list", help="List all tasks")
    
        # Subparser for "list_done" command
        parser_list_done = subparsers.add_parser("list.done", help="All tasks with done status")
    
        # Subparser for "list_done" command
        parser_list_todo = subparsers.add_parser("list.todo", help="All tasks with to do status")
    
        # Subparser for "list_done" command
        parser_list_in_progress = subparsers.add_parser("list.inprogress", help="All tasks with in progress status")
    
    
    
    
        # Parse the arguments
        args = parser.parse_args()
    
        # Execute the appropriate function based on the subcommand
        if args.command == "add":
            add(args.description)
        elif args.command == "delete":
            delete(args.id_delete)
        elif args.command == "update":
            update(args.id_update,args.description)
        elif args.command == "mark_in_progress":
            mark_in_progess(args.id_update_status)
        elif args.command == "mark_done":
            mark_done(args.id_update_task)
        elif args.command == "list":
            list_tasks()
        elif args.command == "list.done":
            list_done()
        elif args.command == "list.todo":
            list_todo()
        elif args.command == "list.inprogress":
            list_in_progress()
        else:
            parser.print_help()

        if __name__ == "__main__":
            main()
    



