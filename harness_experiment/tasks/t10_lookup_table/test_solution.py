from solution import status_message


def test_known_codes():
    assert status_message(200) == "OK"
    assert status_message(404) == "Not Found"
    assert status_message(500) == "Internal Server Error"


def test_rate_limit_code_present():
    assert status_message(429) == "Too Many Requests"


def test_unknown_code_falls_back():
    assert status_message(999) == "Unknown Status"
