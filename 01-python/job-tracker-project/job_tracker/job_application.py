from dataclasses import dataclass,field
from typing import ClassVar
from .validation import normalize_text,validate_status

@dataclass
class JobApplication:

    ALLOWED_STATUSES: ClassVar[frozenset[str]] = frozenset({"applied","interview","rejected","offer"})

    unique_id: int
    company: str
    role: str
    status: str
    date_applied: int
    notes: list[str] = field(default_factory=list)


    def __post_init__(self) -> None:

        self.company = normalize_text(self.company, "company")
        self.role = normalize_text(self.role, "role")
        self.status = validate_status(self.status, self.ALLOWED_STATUSES)


    def change_status(self,new_status: str) -> None:

        self.status = validate_status(new_status, self.ALLOWED_STATUSES)


    def add_note(self, note: str) -> None:

        note = normalize_text(note, "note")

        self.notes.append(note)

        



    






    















