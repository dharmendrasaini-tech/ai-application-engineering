from job_tracker.job_application import JobApplication
import pytest 



def test_create_valid_application() -> None:
    application = JobApplication(
        unique_id=1,
        company=" Google ",
        role=" AI Engineer",
        status= "   INTERVIEW ",
        date_applied=20260927)


    assert application.unique_id == 1
    assert application.company == "Google"
    assert application.role == "AI Engineer"
    assert application.status == "interview"
    assert application.date_applied == 20260927 


def test_blank_company_raises_value_error() -> None:

    with pytest.raises(ValueError):

        JobApplication(
            unique_id=1,
            company="  ",
            role="AI Engineer",
            status="applied",
            date_applied=20260927,
        )

def test_blank_role_raises_value_error() -> None:

    with pytest.raises(ValueError):

        JobApplication(
            unique_id=1,
            company="microsoft",
            role=" ",
            status="applied",
            date_applied=20260927,
        )


def test_invalid_status_raises_value_error() -> None:

    with pytest.raises(ValueError):

        JobApplication(
            unique_id=1,
            company="dell",
            role="software engineer",
            status="super",
            date_applied=20260927,
        )


def test_change_status_updates_status() -> None:

    application = JobApplication(
        unique_id=1,
        company="microsoft",
        role="engineer",
        status="applied",
        date_applied=20260927,
    )

    application.change_status("rejected")

    assert application.status == "rejected"



def test_invalid_status_change_raises_value_error() -> None:

    application = JobApplication(
        unique_id=1,
        company="microsoft",
        role="engineer",
        status="applied",
        date_applied=20260927,
        )


    with pytest.raises(ValueError):

        application.change_status("super")


def test_add_note_adds_valid_note() -> None:

    application = JobApplication(
        unique_id=1,
        company="microsoft",
        role="engineer",
        status="applied",
        date_applied=20260927,
        )

    application.add_note("  Application accepted.")

    assert application.notes == ["Application accepted."]


def test_blank_note_raises_value_error() -> None:

    application = JobApplication(
        unique_id=1,
        company="microsoft",
        role="engineer",
        status="applied",
        date_applied=20260927,
        )



    with pytest.raises(ValueError):
        application.add_note(" ")






