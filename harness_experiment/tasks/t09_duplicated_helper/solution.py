def _validate_short_string(value, field_name, max_length=20):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string")
    if len(value) > max_length:
        raise ValueError(f"{field_name} must be at most {max_length} characters")
    return value.strip()


def validate_username(username):
    return _validate_short_string(username, "username", 20)


def validate_display_name(display_name):
    return _validate_short_string(display_name, "display_name", 20)