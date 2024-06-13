from models.name import create_name, delete_name, update_name, read_names  # Importing functions for CRUD operations on names
from models.task import create_task, delete_task, update_task, read_tasks  # Importing functions for CRUD operations on tasks
from models.label import create_label, delete_label, update_label, read_labels  # Importing functions for CRUD operations on labels
from database.connection import create_db_session  # Importing function to create a database session
from datetime import datetime  # Importing datetime for date operations

def main():
    session = create_db_session()  # Creating a database session
    
    while True:
        print("\nMenu:")
        # List of menu options
        menu_options = [
            "Create Name",
            "Read Names",
            "Update Name",
            "Delete Name",
            "Create Task",
            "Read Tasks",
            "Update Task",
            "Delete Task",
            "Create Label",
            "Read Labels",
            "Update Label",
            "Delete Label",
            "Exit"
        ]
        for index, option in enumerate(menu_options, start=1):
            print(f"{index}. {option}")  # Printing menu options using a tuple (index, option)
        
        choice = input("Enter your choice: ")  # User input for menu choice
        
        if choice == "1":
            # Dictionary to collect user input for creating a name
            name_data = {
                "name": input("Enter name: ").strip(),
                "role": input("Enter role: ").strip()
            }
            if not all(name_data.values()):
                print("Kindly make a valid entry to proceed.")
                continue
            create_name(session, **name_data)  # Creating a name using ORM (Object-Relational Mapping) and dictionaries
        elif choice == "2":
            read_names(session)  # Reading names using ORM and sessions
        elif choice == "3":
            name_id = input("Enter name ID to update: ").strip()
            if not name_id:
                print("Kindly make a valid entry to proceed.")
                continue
            update_name(session, int(name_id))  # Updating a name using ORM and sessions
        elif choice == "4":
            name_id = input("Enter name ID to delete: ").strip()
            if not name_id:
                print("Kindly make a valid entry to proceed.")
                continue
            delete_name(session, int(name_id))  # Deleting a name using ORM and sessions
        elif choice == "5":
            # Dictionary to collect user input for creating a task
            task_data = {
                "title": input("Enter task title: ").strip(),
                "description": input("Enter task description: ").strip(),
                "due_date": input("Enter due date (YYYY-MM-DD): ").strip(),
                "name_id": input("Enter name ID: ").strip()
            }
            if not all(task_data.values()):
                print("Kindly make a valid entry to proceed.")
                continue
            try:
                task_data["due_date"] = datetime.strptime(task_data["due_date"], '%Y-%m-%d').date()
                if task_data["due_date"] < datetime.now().date():
                    print("Due date must be a future date.")
                else:
                    create_task(session, **task_data)  # Creating a task using ORM and dictionaries
            except ValueError:
                print("Invalid date format. Please enter the due date in YYYY-MM-DD format.")
        elif choice == "6":
            read_tasks(session)  # Reading tasks using ORM and sessions
        elif choice == "7":
            task_id = input("Enter task ID to update: ").strip()
            if not task_id:
                print("Kindly make a valid entry to proceed.")
                continue
            update_task(session, int(task_id))  # Updating a task using ORM and sessions
        elif choice == "8":
            task_id = input("Enter task ID to delete: ").strip()
            if not task_id:
                print("Kindly make a valid entry to proceed.")
                continue
            delete_task(session, int(task_id))  # Deleting a task using ORM and sessions
        elif choice == "9":
            # Dictionary to collect user input for creating a label
            label_data = {
                "name": input("Enter label name: ").strip(),
                "task_id": input("Enter task ID: ").strip()
            }
            if not all(label_data.values()):
                print("Kindly make a valid entry to proceed.")
                continue
            create_label(session, **label_data)  # Creating a label using ORM and dictionaries
        elif choice == "10":
            read_labels(session)  # Reading labels using ORM and sessions
        elif choice == "11":
            label_id = input("Enter label ID to update: ").strip()
            if not label_id:
                print("Kindly make a valid entry to proceed.")
                continue
            update_label(session, int(label_id))  # Updating a label using ORM and sessions
        elif choice == "12":
            label_id = input("Enter label ID to delete: ").strip()
            if not label_id:
                print("Kindly make a valid entry to proceed.")
                continue
            delete_label(session, int(label_id))  # Deleting a label using ORM and sessions
        elif choice == "13":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
