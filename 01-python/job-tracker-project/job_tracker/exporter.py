from pathlib import Path
from .job_application import JobApplication
from .exceptions import StorageError

def export_applications(applications: list[JobApplication], file_path: Path) -> None:

    try:

        with file_path.open("w", encoding="utf-8") as file:
            for application in applications:
                file.write(f"ID: {application.unique_id}\n")
                file.write(f"Company: {application.company}\n")
                file.write(f"Role: {application.role}\n")
                file.write(f"Status: {application.status}\n")
                file.write(f"Date_applied: {application.date_applied}\n")
                file.write("Notes: \n")

                for note in application.notes:
                    file.write(f"- {note}\n")

                file.write("-" * 20 + "\n\n")


    except OSError as exc:
        raise StorageError("Unable to export application data.") from exc

    