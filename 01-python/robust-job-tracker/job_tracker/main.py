from .application import JobApplication
from .exceptions import ApplicationNotFoundError
from .tracker import JobTracker
import logging


logging.basicConfig(
    filename= "job_tracker.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)



logger = logging.getLogger(__name__)


def main() -> None:

    tracker = JobTracker()
    logger.info("Job Tracker started.")


    try:

        while True:

  
            print("=== Job Tracker ===")
            print("1. Add application")
            print("2. Update application status")
            print("3. List applications")
            print("4. Exit")

            choice = input("Enter your choice: ").strip()

            logger.debug("Menu choice received: %s", choice)

            


            if choice == "1":

                company = input("Enter company name: ")
                role = input("Enter role: ")

                try:
                    application = JobApplication(company,role)
                    tracker.add_application(application)

                except ValueError as error:
                    print(f"Could not add application: {error}")
                    logger.warning("Application creation failed: %s",error)

                else:
                    print("Application added successfully.")
                    logger.info("Application added: company=%s, role=%s",application.company, application.role)


            elif choice == "2":
                application_number = input("Enter application number: ").strip()
                new_status = input("Enter new status: ")

                try:
                    application_number = int(application_number)

                except ValueError as error:
                    print("Application number must be a digit.")
                    logger.warning("Invalid application number input: %s",error)

                else:
                    try:
                        tracker.update_status(application_number,new_status)

                    except ApplicationNotFoundError as error:
                        print(f"Could not update application. {error}")
                        logger.warning("Application not found: %s",error)

                    except ValueError as error:
                        print(f"Invalid status: {error}")
                        logger.warning("Status not valid: %s", error)

                    else:
                        print("Status updated successfully.")
                        logger.info("Status updated successfully: Application number=%s, new_status=%s", application_number, new_status)


                
            elif choice == "3":

                applications = tracker.list_applications()

                if not applications:
                    print("No applications found.")

                else:
                    for number , application in enumerate(applications, start=1):
                        print(
                            f"{number}. "
                            f"{application.company} | "
                            f"{application.role} | "
                            f"{application.status}"
                        )


            elif choice == "4":
                logger.info("Program Exited.")
                break

            else:
                print("Invalid input")
                logger.warning("Unsupported menu choice: %s",choice)
                

                    

    except Exception:

        logger.exception("Unexpected failure while processing menu action.")

        print("An unexpected error occured. Please try again")

        raise















if __name__ == "__main__":
    main()