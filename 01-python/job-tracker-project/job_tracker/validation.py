

def normalize_text(text: str, field: str) -> str:
    stripped_text = text.strip()

    if not stripped_text:
        raise ValueError(f"{field} cannot be blank.")

    return stripped_text


def validate_status(status: str, allowed_statuses: frozenset[str]) -> str:


    normalized_status = status.strip().lower()

    if normalized_status not in allowed_statuses:
        raise ValueError(f"Invalid status: {normalized_status}")

    return normalized_status

    
