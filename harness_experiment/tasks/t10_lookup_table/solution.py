def status_message(code):
    """Return a human-readable message for an HTTP-like status code."""
    status_messages = {
        200: "OK",
        201: "Created",
        400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Not Found",
        500: "Internal Server Error",
        429: "Too Many Requests"
    }
    return status_messages.get(code, "Unknown Status")