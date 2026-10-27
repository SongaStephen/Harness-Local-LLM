from solution import mean

def test_normal_case():
    assert mean([1, 2, 3]) == 2

def test_single_value():
    assert mean([5]) == 5

def test_empty_list_returns_none():
    assert mean([]) is None
