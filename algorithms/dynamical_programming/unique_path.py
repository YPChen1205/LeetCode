def unique_paths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    dp = [1 for col in range(n)]
    for r in range(1, m):
        for c in range(1, n):
            dp[c] = dp[c] + dp[c-1]

    return dp[n-1]


if __name__ == '__main__':
    print(unique_paths(7,3)) #28