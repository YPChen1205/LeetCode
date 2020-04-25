def longest_common_subsequence(text1, text2):
    """
    :type text1: str
    :type text2: str
    :rtype: int
    """
    ln1 = len(text1)
    ln2 = len(text2)
    dp = [[0 for j in range(ln2+1)] for i in range(ln1+1)]
    for i in range(1, ln1+1):
        for j in range(1, ln2+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[ln1][ln2]


if __name__ == '__main__':
    print(longest_common_subsequence(text1="abcde", text2="ace"))  # 3
    print(longest_common_subsequence(text1="abc", text2="def"))  # 0
    print(longest_common_subsequence(text1="abc", text2="abc"))  # 3
