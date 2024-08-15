import argparse
from datetime import datetime
import json

file_path = "data.json"

# Get current date and time
date_time_now = datetime.now()
date_time_str = date_time_now.strftime("%d/%m/%Y %H:%M")

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
    print(f"Task added successfully (ID: {new_id})")

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
            task["description"] = description;
            task["updateAt"] = date_time_str
            update = True
            break

    #Return the result
    if update:
        print(f"Task of ID {id_update} updated successfully.")
    else:
        print(f"Task of ID {id_update} not found.")

    # Save the updated list of tasks from the file
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

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        data = []

    update = False
    for index, task in enumerate(data):
        if task.get("id") == id_update_task:
            task["status"] = "done";
            task["updateAt"] = date_time_str
            update = True
            break

    if update:
        print("The task with ID {}, is done".format(id_update_task))
    else:
        print("The task with ID {}, is not found".format(id_update_task))

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4,ensure_ascii=False)


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
    subparser_update_done = subparsers.add_parser("Done", help="Update the status with is done")
    subparser_update_done.add_argument("id_update_task", type=str, help="Task id for update with is done")

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
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
