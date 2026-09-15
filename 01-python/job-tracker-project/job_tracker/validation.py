

def normalize_text(text: str, field_name: str) -> str:
    normalized_text = text.strip()

    if not normalized_text:
        raise ValueError(f"{field_name} cannot be blank.")

    return normalized_text


def validate_status(status: str, allowed_statuses: set[str]) -> str:
    normalized_status = status.strip().lower()

    if normalized_status not in allowed_statuses:
        raise ValueError("Invalid status.")

    return normalized_status


