import time
from solution import count_partitions


def _ground_truth(n, k):
    """Independent DP reference implementation (same recurrence, tabulated)."""
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            dp[i][j] = dp[i - 1][j - 1] + (dp[i - j][j] if i - j >= 0 else 0)
    return dp[n][k]


def test_small_values_correct():
    assert count_partitions(10, 3) == _ground_truth(10, 3)
    assert count_partitions(7, 2) == _ground_truth(7, 2)


def test_completes_quickly_on_larger_input():
    started = time.time()
    result = count_partitions(100, 30)
    elapsed = time.time() - started
    assert result == _ground_truth(100, 30)
    assert elapsed < 2.0, f"took {elapsed:.1f}s -- looks unmemoized"
