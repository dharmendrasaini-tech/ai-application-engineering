from dataclasses import dataclass,field
from .validation import normalize_text,validate_status
from typing import ClassVar


@dataclass
class JobApplication:

    ALLOWED_STATUSES: ClassVar[set[str]] = {"applied","interview","rejected","offer"}

    company: str
    role: str
    status: str = "applied"
    notes: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.company = normalize_text(self.company,"company")
        self.role = normalize_text(self.role, "role")
        self.status = validate_status(self.status,self.ALLOWED_STATUSES)


    def change_status(self,new_status:str) -> None:

        new_status = validate_status(new_status,self.ALLOWED_STATUSES)

        self.status = new_status


    def add_note(self,note:str) -> None:

        note = normalize_text(note,"note")

        self.notes.append(note)


    def get_summary(self) -> str:

        return f"Company: {self.company}, Role: {self.role}, Status: {self.status}, Notes: {self.notes}"

    

    













