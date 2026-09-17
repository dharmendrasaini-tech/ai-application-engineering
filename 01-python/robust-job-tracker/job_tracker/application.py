from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)

@dataclass
class JobApplication:

    ALLOWED_STATUSES = frozenset({"applied", "interview", "rejected", "offer"})

    company: str
    role: str
    status: str = "applied"

    def __post_init__(self) -> None:

        normalized_company = self.company.strip()
        normalized_role = self.role.strip()
        normalized_status = self.status.strip().lower()

        if not normalized_company:
            raise ValueError("Company cannot be blank.")

        if not normalized_role:
            raise ValueError("Role cannot be blank.")

        if  normalized_status not in self.ALLOWED_STATUSES:
            raise ValueError("Invalid status.")
              

        self.company = normalized_company
        self.role = normalized_role
        self.status = normalized_status


    def change_status(self,new_status: str) -> None:

        normalized_new_status = new_status.strip().lower()

        if normalized_new_status not in self.ALLOWED_STATUSES:
            raise ValueError("Invalid status")


        self.status = normalized_new_status

    


