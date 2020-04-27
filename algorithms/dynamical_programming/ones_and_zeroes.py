def find_max_form(strs, m, n):
    """
    :type strs: List[str]
    :type m: int
    :type n: int
    :rtype: int
    """
    if not (strs and len(strs)):
        return 0
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
    for s in strs:
        zeros = 0
        ones = 0
        for c in s:
            if c == '0':
                zeros += 1
            else:
                ones += 1
        for i in range(m, zeros - 1, -1):
            for j in range(n, ones - 1, -1):
                dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones]+1)
    return dp[m][n]


if __name__ == '__main__':
    print(find_max_form(["10", "0", "1"], 1, 1))
