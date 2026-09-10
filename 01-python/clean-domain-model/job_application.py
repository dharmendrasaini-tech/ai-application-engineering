# Clean Domain Model Task — Job Application

from dataclasses import dataclass,field

@dataclass
class JobApplication:

    ALLOWED_STATUSES = {"applied","interview","rejected","offer"}


    company: str
    role: str
    status: str = "applied"
    notes: list[str] = field(default_factory=list)

    def __post_init__(self):

        self.company = self.company.strip()
        self.role = self.role.strip()
        self.status = self.status.strip().lower()

        if not self.company:
            raise ValueError("Company cannot be empty.")

        if not self.role:
            raise ValueError("Role cannot be empty.")

        if not self.status:
            raise ValueError("Status cannot be empty.")
        

        if self.status not in self.ALLOWED_STATUSES:
            raise ValueError("Invalid status.")


    def change_status(self,new_status):

        new_status = new_status.strip().lower()

        if not new_status:
            raise ValueError("New status cannot be empty.")

        if new_status not in self.ALLOWED_STATUSES:
            raise ValueError("Invalid status.")


        self.status = new_status

    def add_note(self,note):

        note = note.strip()

        if not note:
            raise ValueError("Note cannot be blank.")

        self.notes.append(note)

    def get_summary(self):
        return f"Company: {self.company} | Role: {self.role} | Status: {self.status} | Notes: {len(self.notes)}"



# #6

# job1 = JobApplication("OpenAI", "AI Engineer")

# job2 = JobApplication("Anthropic", "Backend Engineer")


# job1.add_note("Applied through website")

# print(job1.notes)
# print(job2.notes)

# # job1.notes should contain the note
# # job2.notes must still be []

# #Both works 


# #7 

# job3 = JobApplication("OpenAI", "AI Engineer")
# job4 = JobApplication("OpenAI", "AI Engineer")

# print(job3 == job4)

# job3.add_note("Applied online")

# print(job3 == job4)


# # notes participate because every field participates unless we mark compare=False
# # Dataclass fields participate in generated equality by default , unless they are declared with compare = False

        



        

        



