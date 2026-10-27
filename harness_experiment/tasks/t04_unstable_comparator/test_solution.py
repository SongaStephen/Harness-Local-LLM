import functools
from solution import compare_priority


def test_equal_priority_returns_zero():
    a = {"priority": 5}
    b = {"priority": 5}
    assert compare_priority(a, b) == 0


def test_higher_priority_sorts_first():
    a = {"priority": 10}
    b = {"priority": 5}
    assert compare_priority(a, b) < 0


def test_lower_priority_sorts_last():
    a = {"priority": 3}
    b = {"priority": 8}
    assert compare_priority(a, b) > 0


def test_sort_matches_reverse_numeric_order():
    tasks = [
        {"priority": 1, "id": "a"},
        {"priority": 5, "id": "b"},
        {"priority": 5, "id": "c"},
        {"priority": 3, "id": "d"},
    ]
    ordered = sorted(tasks, key=functools.cmp_to_key(compare_priority))
    priorities = [t["priority"] for t in ordered]
    assert priorities == sorted(priorities, reverse=True)
