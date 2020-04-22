def integer_break(n):
    """
    :type n: int
    :rtype: int
    """
    dp = [0 for i in range(n + 1)]
    for i in range(2, n + 1):
        for j in range(1, i):
            dp[i] = max(dp[i], max(j * dp[i - j], j * (i - j)))
    return dp[n]


if __name__ == '__main__':
    print(integer_break(10))
