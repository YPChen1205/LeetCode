def num_decodings(s):
    """
    :type s: str
    :rtype: int
    """
    if not (s and len(s)):
        return 0
    n = len(s)
    dp = [0 for i in range(n + 1)]
    dp[0] = 1
    if s[0] != '0':
        dp[1] = 1
    for i in range(2, n + 1):
        one = int(s[i - 1:i])
        if one != 0:
            dp[i] += dp[i - 1]
        if s[i - 2] == '0':
            continue
        two = int(s[i - 2: i])
        if two <= 26:
            dp[i] += dp[i - 2]
    return dp[n]


if __name__ == '__main__':
    print(num_decodings('216'))
