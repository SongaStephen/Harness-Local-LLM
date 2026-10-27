def days_between(date1, date2):
    """Return the number of days between two (year, month, day) tuples
    that fall in the same year, date2 on or after date1."""
    def day_of_year(date):
        year, month, day = date
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # Check for leap year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_month[1] = 29  # February has 29 days in a leap year
        return sum(days_in_month[:month - 1]) + day

    y1, m1, d1 = date1
    y2, m2, d2 = date2
    if y1 != y2:
        raise NotImplementedError("cross-year ranges are not supported")
    return day_of_year(date2) - day_of_year(date1)