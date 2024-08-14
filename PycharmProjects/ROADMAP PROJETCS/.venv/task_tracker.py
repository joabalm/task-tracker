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
    with open(file_path, "r") as file:
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
        "status": "",
        "creatAt": date_time_str,
        "updateAt": ""
    }

    # Append the new task to the list
    data.append(new_task)

    # Save the updated list of tasks back to the file
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    #
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
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)



# Function to update the task
def update(id_update, description, status):

    # Load the JSON data from the file
    with open(file_path, "r") as file:
        data = json.load(file)  # Ensure this is a list

    # If data is not a list, initialize it as a list
    if not isinstance(data, list):
        data = []

    # Identify the id and create the update
    for index, task in enumerate(data):
        id_update = int(id_update)
        if task.get("id") == id_update:
            update_task = {
                "id": 6,
                "description": description,
                "status": status,
                "creatAt": "14/08/2024 15:42",
                "updateAt": date_time_str
            }
            break
    # Append the new task to the list
    data.append(update_task)

    # Save the updated list of tasks to the file
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)




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

    # Parse the arguments
    args = parser.parse_args()

    # Execute the appropriate function based on the subcommand
    if args.command == "add":
        add(args.description)
    elif args.command == "delete":
        delete(args.id_delete)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
