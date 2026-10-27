from solution import days_between


def test_non_leap_year_within_january():
    assert days_between((2023, 1, 1), (2023, 1, 31)) == 30


def test_non_leap_year_into_march():
    assert days_between((2023, 1, 1), (2023, 3, 1)) == 59


def test_leap_year_into_march():
    # 2024 is a leap year: Jan (31) + Feb (29) = 60 days from Jan 1 to Mar 1.
    assert days_between((2024, 1, 1), (2024, 3, 1)) == 60


def test_leap_year_within_february():
    assert days_between((2024, 2, 1), (2024, 2, 29)) == 28
