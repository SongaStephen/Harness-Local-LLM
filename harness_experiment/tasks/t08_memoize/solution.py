from functools import lru_cache

@lru_cache(None)
def count_partitions(n, k):
    """Count the number of ways to partition integer n into exactly k
    positive parts (order doesn't matter). Correct but unmemoized --
    exponential blowup for moderately large n/k."""
    if k == 0:
        return 1 if n == 0 else 0
    if n <= 0:
        return 0
    return count_partitions(n - 1, k - 1) + count_partitions(n - k, k)