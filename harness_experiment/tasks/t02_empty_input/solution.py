def mean(values):
    """Return the arithmetic mean of `values`."""
    if not values:
        return None
    return sum(values) / len(values)