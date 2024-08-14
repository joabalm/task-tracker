import argparse
from datetime import datetime
import json

file_path = "data.json"

date_time_str = date_time_now.strftime("%d/%m/%Y %H:%M")

# Function to add a new task
def add(description):
    # Load the JSON data from the file
    with open(file_path, "r") as file:
        data = json.load(file)  # Ensure this is a list

    # If data is not a list, initialize it as a list
    if not isinstance(data, list):
        data = []

    # Get current date and time
    date_time_now = datetime.now()


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

def update(id_delete, description):

    # Load the JSON data from the file
    with open(file_path, "r") as file:
        data = json.load(file)  # Ensure this is a list

    # If data is not a list, initialize it as a list
    if not isinstance(data, list):
        data = []

    # scroll through the list to find the item
    for item in data:
        if item["id"] == id_delete:
            data.remove(item)
            break

    #
    print(f"Task deleted successfully (ID: {id_delete})")




def main():
    parser = argparse.ArgumentParser(
        prog="task-manager",
        description="Task Manager CLI",
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", type=str, help="The description of the new task")

    args = parser.parse_args()

    if args.command == "add":
        add(args.description)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
