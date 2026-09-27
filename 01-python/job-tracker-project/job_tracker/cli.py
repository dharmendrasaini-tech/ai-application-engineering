import logging
from .job_tracker import JobTracker
from .job_application import JobApplication
from .exceptions import ApplicationNotFoundError
from .exceptions import StorageError
from pathlib import Path
from .exporter import export_applications
from .api_client import ApiClient
from .exceptions import ExternalServiceError
from .json_storage import JsonStorage





logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"

)


def display_menu() -> None:
    print("1. Add application")
    print("2. List applications")
    print("3. View application")
    print("4. Update status")
    print("5. Add note")
    print("6. Search applications")
    print("7. Filter applications")
    print("8. Delete application")
    print("9. Export")
    print("10. API feature")
    print("0. Exit")


def display_application(application: JobApplication) -> None:

    print(
        f"ID: {application.unique_id}\n"
        f"Company: {application.company}\n"
        f"Role: {application.role}\n"
        f"Status: {application.status}\n"
        f"Date_applied: {application.date_applied}\n"
    )

    print("Notes - \n")
    for note in application.notes:
        print(f"{note}\n")

    

def main() -> None:

    tracker = JobTracker()
    api_client = ApiClient()

    storage = JsonStorage(Path("applications.json"))

    try:
        saved_applications = storage.load()

        for application in saved_applications:
            tracker.add_application(application)

    except StorageError as exc:
        print(f"Error loading applications: {exc}")
        return




    while True:


        display_menu()

        menu_choice = input("Enter menu choice: ").strip()

        if menu_choice == "1":

            try:


                unique_id = int(input("Enter unique ID: "))
                company = input("Enter company: ")
                role = input("Enter role: ")
                status = input("Enter status: ")
                date_applied = int(input("Enter date applied: "))

                application = JobApplication(unique_id=unique_id, company=company, role=role, status=status, date_applied=date_applied)

                tracker.add_application(application)

                storage.save(tracker.list_applications())

                print("Application added successfully.")


            except ValueError as exc:
                print(f"Error: {exc}")

            except StorageError as exc:
                print(f"Storage error: {exc}")


        elif menu_choice == "2":

            applications = tracker.list_applications()

            if not applications:
                print("No applications found.")


            else:      
                for application in applications:
                    display_application(application)


        elif menu_choice == "3":

            try:
                
                unique_id = int(input("Enter unique ID: "))

                application = tracker.get_application_by_id(unique_id)

                display_application(application)

            except ApplicationNotFoundError as exc:
                print(f"Error: {exc}")

            except ValueError:
                print("ID must be a number.")


        elif menu_choice == "4":

            try:

                unique_id = int(input("Enter unique ID: "))
                new_status = input("Enter new status: ")

                tracker.update_application_status(unique_id=unique_id, new_status=new_status)


                storage.save(tracker.list_applications())

                print("Application status updated successfully.")

            except ValueError as exc:
                print(f"Error: {exc}")

            except ApplicationNotFoundError as exc:
                print(f"Error: {exc}")

            except StorageError as exc:
                print(f"Storage error: {exc}")

            

        elif menu_choice == "5":

            try:
                unique_id = int(input("Enter unique ID: "))

                note = input("Enter note: ")

                tracker.add_note(unique_id=unique_id, note=note)

                storage.save(tracker.list_applications())

                print("Note added successfully.")


            except ValueError as exc:
                print(f"Error: {exc}")

            except ApplicationNotFoundError as exc:
                print(f"Error: {exc}")

            except StorageError as exc:
                print(f"Storage error: {exc}")



        elif menu_choice == "6":

            try:
                
                query = input("Enter company name or role name: ")

                applications = tracker.search_applications(query=query)

                if not applications:
                    print("No application found.")

                else:

                    for application in applications:
                        display_application(application)


            except ValueError as exc:
                print(f"Error: {exc}")


        elif menu_choice == "7":

            try:

                status = input("Enter status: ")

                found = False

                for application in tracker.iter_by_status(status):

                    display_application(application)

                    found = True

                if not found:
                    print("No applications found.")

            except ValueError as exc:
                print(f"Error: {exc}")



        elif menu_choice == "8":

            try:

                unique_id = int(input("Enter unique ID: "))

                tracker.delete_application(unique_id=unique_id)

                storage.save(tracker.list_applications())

                print("Application deleted successfully.")

            except ValueError as exc:
                print(f"Error: {exc}")

            except ApplicationNotFoundError as exc:
                print(f"Error: {exc}")

            except StorageError as exc:
                print(f"Storage error: {exc}")


        elif menu_choice == "9":

            try:

                applications = tracker.list_applications()

                file_path_input = input("Enter file path to export: ").strip()

                file_path = Path(file_path_input)

                export_applications(applications=applications, file_path=file_path)

                print("Applications exported successfully.")

            except StorageError as exc:
                print(f"Error: {exc}")


        elif menu_choice == "10":

            try:
                post_id = int(input("Enter post ID"))

                post = api_client.fetch_post(post_id=post_id)

                print(f"Post ID: {post['id']}")
                print(f"User ID: {post['userId']}")
                print(f"Title: {post['title']}")
                print(f"Body: {post['body']}")

            except ValueError:
                print("Post ID must be a number.")

            except ExternalServiceError as exc:
                print(f"Error: {exc}")


        elif menu_choice == "0":
            print("Goodbye")
            break

        else:
            print("Invalid menu choice.")




if __name__ == "__main__":
    main()















            

            









