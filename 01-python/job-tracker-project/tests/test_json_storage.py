import pytest
import json
from job_tracker.job_application import JobApplication
from job_tracker.json_storage import JsonStorage
from job_tracker.exceptions import StorageError

def test_save_and_load_applications(tmp_path) -> None:

    file_path = tmp_path / "applications.json"

    storage = JsonStorage(file_path)


    application = JobApplication(
        unique_id=1,
        company="Google",
        role="AI Engineer",
        status="applied",
        date_applied=20260927,
    )

    storage.save([application])

    loaded_applications = storage.load()

    assert loaded_applications == [application]




