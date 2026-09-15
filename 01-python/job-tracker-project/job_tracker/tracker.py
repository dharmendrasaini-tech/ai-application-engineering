from .application import JobApplication
from .stats import counts_by_status
from .validation import validate_status


class JobTracker:
    def __init__(self):
        self.applications = []

    def add_application(self,application) -> None:

        if not isinstance(application, JobApplication):
            raise TypeError("application must be a JobApplication instance.")

        self.applications.append(application)

    def total_applications(self) -> int:

        return len(self.applications)


    def find_by_status(self,status:str) -> list[JobApplication]:

        validated_status = validate_status(status,JobApplication.ALLOWED_STATUSES)

        matching_applications: list[JobApplication] = []

        for application in self.applications:
            if application.status == validated_status:
                matching_applications.append(application)

        return matching_applications


    def get_status_counts(self) -> dict[str,int]:

        return counts_by_status(self.applications)

    



