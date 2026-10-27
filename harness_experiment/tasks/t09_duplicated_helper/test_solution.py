import pytest
from solution import validate_username, validate_display_name


def test_username_valid_and_stripped():
    assert validate_username(" alice ") == "alice"


def test_username_too_long_rejected():
    with pytest.raises(ValueError):
        validate_username("a" * 21)


def test_display_name_valid_and_stripped():
    assert validate_display_name(" Bob ") == "Bob"


def test_display_name_at_limit_allowed():
    assert validate_display_name("a" * 20) == "a" * 20


def test_display_name_too_long_rejected():
    with pytest.raises(ValueError):
        validate_display_name("a" * 21)
