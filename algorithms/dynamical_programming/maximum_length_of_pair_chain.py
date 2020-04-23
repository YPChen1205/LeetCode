def find_longest_chain(pairs):
    """
    :type pairs: List[List[int]]
    :rtype: int
    """
    n = len(pairs)
    dp = [1 for i in range(n)]
    for i in range(n):
        for j in range(i):
            if pairs[j][1] < pairs[i][0]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


if __name__ == '__main__':
    print(find_longest_chain([[1, 2], [2, 3], [3, 4]]))
