def create_user(payload):
    """Create a user record from a request payload dict.
    Expected keys: 'name' (non-empty str), 'age' (int, 0-150).
    Raises ValueError for invalid input.
    """
    if 'name' not in payload or not payload['name'].strip():
        raise ValueError("The 'name' field is missing or empty/whitespace.")
    if 'age' not in payload:
        raise ValueError("The 'age' field is missing.")
    if not isinstance(payload['age'], int):
        raise ValueError("The 'age' field must be an integer.")
    if payload['age'] < 0 or payload['age'] > 150:
        raise ValueError("The 'age' field must be an integer between 0 and 150.")

    return {"name": payload["name"], "age": payload["age"]}