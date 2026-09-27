import pytest
from job_tracker.job_tracker import JobTracker
from job_tracker.job_application import JobApplication
from job_tracker.exceptions import ApplicationNotFoundError



def test_create_valid_job_tracker() -> None:

    tracker = JobTracker()

    assert tracker.list_applications() == []


def test_add_application_adds_valid_application() -> None:

    tracker = JobTracker()

    application = JobApplication(
        unique_id=1,
        company=" Google ",
        role=" AI Engineer",
        status= "   INTERVIEW ",
        date_applied=20260927)

    tracker.add_application(application)

    assert tracker.list_applications() == [application]


def test_add_application_with_duplicate_id_raises_value_error() -> None:

    tracker = JobTracker()

    application = JobApplication(
        unique_id=1,
        company=" Google ",
        role=" AI Engineer",
        status= "   INTERVIEW ",
        date_applied=20260927)


    tracker.add_application(application)

    application2 = JobApplication(
        unique_id=1,
        company=" Cred ",
        role=" AI Engineer",
        status= "   applied ",
        date_applied=20260927)

    with pytest.raises(ValueError):
        tracker.add_application(application2)

    

def test_get_application_by_id_returns_correct_application() -> None:

    tracker = JobTracker()


    application = JobApplication(
        unique_id=1,
        company=" Google ",
        role=" AI Engineer",
        status= "   INTERVIEW ",
        date_applied=20260927)

    tracker.add_application(application)

    assert tracker.get_application_by_id(1) == application


def test_get_application_by_id_raises_for_mising_id() -> None:

    tracker = JobTracker()

    application = JobApplication(
        unique_id=1,
        company=" Google ",
        role=" AI Engineer",
        status= "   INTERVIEW ",
        date_applied=20260927)

    tracker.add_application(application)

    with pytest.raises(ApplicationNotFoundError):
        tracker.get_application_by_id(99)


def test_update_application_status_updates_status() -> None:


    tracker = JobTracker()

    application = JobApplication(
        unique_id=1,
        company=" Google ",
        role=" AI Engineer",
        status= "   INTERVIEW ",
        date_applied=20260927)


    tracker.add_application(application)


    tracker.update_application_status(unique_id=1,new_status="rejected")

    assert application.status == "rejected"


def test_delete_application_deletes_application() -> None:


    tracker = JobTracker()

    application = JobApplication(
        unique_id=1,
        company=" Google ",
        role=" AI Engineer",
        status= "   INTERVIEW ",
        date_applied=20260927)


    tracker.add_application(application)

    tracker.delete_application(1)

    assert tracker.list_applications() == []


def test_add_note_adds_note_to_application() -> None:


    tracker = JobTracker()

    application = JobApplication(
        unique_id=1,
        company=" Google ",
        role=" AI Engineer",
        status= "   INTERVIEW ",
        date_applied=20260927)

    tracker.add_application(application)

    tracker.add_note(unique_id=1, note="Application approved.")

    assert application.notes == ["Application approved."]


def test_search_application_returns_valid_applications() -> None:


    tracker = JobTracker()

    application = JobApplication(
        unique_id=1,
        company=" Google ",
        role=" AI Engineer",
        status= "   INTERVIEW ",
        date_applied=20260927)


    tracker.add_application(application)


    applications = tracker.search_applications(query="AI Engineer")

    assert applications == [application]


def test_iter_by_status_returns_matching_applications() -> None:



    tracker = JobTracker()

    application1 = JobApplication(
        unique_id=1,
        company=" Google ",
        role=" AI Engineer",
        status= "   INTERVIEW ",
        date_applied=20260927)

    application2 = JobApplication(
        unique_id=2,
        company="Microsoft",
        role="Backend Engineer",
        status="applied",
        date_applied=20260927,
    )

    tracker.add_application(application1)
    tracker.add_application(application2)

    applications = list(tracker.iter_by_status("interview"))

    assert applications == [application1]









    






