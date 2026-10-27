import pytest
from solution import create_user


def test_valid_payload():
    assert create_user({"name": "Alice", "age": 30}) == {"name": "Alice", "age": 30}


def test_missing_name_raises_value_error():
    with pytest.raises(ValueError):
        create_user({"age": 30})


def test_empty_name_raises_value_error():
    with pytest.raises(ValueError):
        create_user({"name": "", "age": 30})


def test_negative_age_raises_value_error():
    with pytest.raises(ValueError):
        create_user({"name": "Bob", "age": -1})


def test_age_out_of_range_raises_value_error():
    with pytest.raises(ValueError):
        create_user({"name": "Bob", "age": 200})
