"""Climbing Stairs Solution."""


def climbing_stairs(n):
    """Find how many ways to reach."""
    # import pdb; pdb.set_trace()
    if n <= 2:
        return n
    dp = [0 for __ in range(n)]
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n - 1]
