from pathlib import Path
from dataclasses import asdict
import json
import logging

from .job_application import JobApplication
from .exceptions import StorageError

logger = logging.getLogger(__name__)

class JsonStorage:
    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path

    def save(self, applications: list[JobApplication]) -> None:

        data = [asdict(application) for application in applications]

        try:
            with self.file_path.open("w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

            logger.info("Application data saved.")

        except OSError as exc:
            logger.exception("Failed to save application data.")
            raise StorageError("Unable to save application data.") from exc


    def load(self) -> list[JobApplication]:

        if not self.file_path.exists():
            return []

        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                content = file.read()

            if not content.strip():
                return []

            data = json.loads(content)

            

        except json.JSONDecodeError as exc:
            logger.exception("Stored JSON data is malformed.")
            raise StorageError("Stored JSON data is malformed.") from exc

        except OSError as exc:
            logger.exception("Failed to load application data.")
            raise StorageError("Failed to load application data.") from exc
        


        try:

            applications = [JobApplication(**item) for item in data]

        except (TypeError, ValueError) as exc:
            logger.exception("Stored application data is invalid.")
            raise StorageError("Stored application data is invalid.") from exc


        logger.info("Application data loaded.")
        return applications


        
        

        





        
