from job_tracker.validation import normalize_text,validate_status


def test_normalize_text_strips_whitespace() -> None:
    assert normalize_text(" Google", "  company") == "Google"


def test_validate_status_normalizes_valid_status() -> None:
    allowed_statuses = frozenset({"applied", "interview", "rejected", "offer"})

    result = validate_status("INTERVIEW  ", allowed_statuses)

    assert result == "interview"