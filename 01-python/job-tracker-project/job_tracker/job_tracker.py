from .job_application import JobApplication
from .exceptions import ApplicationNotFoundError
from .validation import normalize_text , validate_status
from collections.abc import Iterator
import logging


logger = logging.getLogger(__name__)





class JobTracker:

    def __init__(self) -> None:
        self.applications: list[JobApplication] = []

    def add_application(self,application: JobApplication) -> None:

        for existing_application in self.applications:
            if existing_application.unique_id == application.unique_id:
                raise ValueError(f"Application id {application.unique_id} already exists.")

        self.applications.append(application)

        logger.info("Application added with id=%s company=%s", application.unique_id, application.company)

    def list_applications(self) -> list[JobApplication]:

        return self.applications.copy()


    def get_application_by_id(self, unique_id: int) -> JobApplication:

        for application in self.applications:
            if unique_id == application.unique_id:
                return application


        raise ApplicationNotFoundError("Application not found.")
        
         
    def update_application_status(self,unique_id: int, new_status: str) -> None:

        application = self.get_application_by_id(unique_id)

        application.change_status(new_status)

        logger.info("Application status updated id=%s status=%s",unique_id, application.status)
    
    



    def delete_application(self, unique_id: int) -> None:

        application = self.get_application_by_id(unique_id)

        self.applications.remove(application)

        logger.info("Application deleted with id=%s", unique_id)


    def add_note(self, unique_id: int, note: str) -> None:

        application = self.get_application_by_id(unique_id)

        application.add_note(note)

    def search_applications(self, query: str) -> list[JobApplication]:

        search_result = []       
        normalized_query = normalize_text(query, "company or role").lower()

        for application in self.applications:
            if application.company.lower() == normalized_query or application.role.lower() == normalized_query:
                search_result.append(application)

        return search_result


    def iter_by_status(self, status: str) -> Iterator[JobApplication]:

        validated_status = validate_status(status, JobApplication.ALLOWED_STATUSES)

        for application in self.applications:
            if application.status == validated_status:
                yield application


        



    # def filter_applications_by_status(self, status: str) -> list[JobApplication]:

    #     filtered_applications = []

    #     validated_status = validate_status(status, JobApplication.ALLOWED_STATUSES)

    #     for application in self.applications:
    #         if application.status == validated_status:
    #             filtered_applications.append(application)

    #     return filtered_applications

    
    def get_application_summary(self, unique_id: int) -> JobApplication:

        return self.get_application_by_id(unique_id)

    

    


    

    



    


    






















        

        



        


    
            

    












