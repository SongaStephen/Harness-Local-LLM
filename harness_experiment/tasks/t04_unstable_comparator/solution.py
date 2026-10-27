def compare_priority(a, b):
    """Comparator for sorting task dicts by 'priority' (higher priority first).
    Intended for use with functools.cmp_to_key."""
    if a["priority"] > b["priority"]:
        return -1
    elif a["priority"] < b["priority"]:
        return 1
    else:
        return 0
    # Fixed: now returns 0 for equal priorities, satisfying the comparator
    # contract (a==b must give 0) and ensuring stable, transitive ordering.