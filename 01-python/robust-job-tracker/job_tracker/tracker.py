from .application import JobApplication
from .exceptions import ApplicationNotFoundError
import logging

logger = logging.getLogger(__name__)


class JobTracker:

    def __init__(self) -> None:
        self._applications: list[JobApplication] = []


    def add_application(self,application:JobApplication) -> None:

        if not isinstance(application, JobApplication):
            raise TypeError("Application must be an instance of JobApplication class.")

        self._applications.append(application)

    def list_applications(self) -> list[JobApplication]:
        return self._applications.copy()


    def get_application(self,number:int) -> JobApplication:

        if not 1 <= number <= len(self._applications):
            raise ApplicationNotFoundError("Application not found with this number.")

        application_index = number - 1

        return self._applications[application_index]


    def update_status(self,number:int,new_status: str) -> None:

        application = self.get_application(number)
        application.change_status(new_status)









        

    

        



    


    