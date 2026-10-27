from solution import paginate

def test_full_page():
    items = list(range(10))
    assert paginate(items, page=1, page_size=5) == [0, 1, 2, 3, 4]

def test_second_page():
    items = list(range(10))
    assert paginate(items, page=2, page_size=5) == [5, 6, 7, 8, 9]

def test_page_size_one():
    items = list(range(3))
    assert paginate(items, page=2, page_size=1) == [1]
