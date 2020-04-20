def min_path_sum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    m = len(grid)
    n = len(grid[0])
    if not (m and n):
        return 0
    dp = [0 for i in range(n)]
    for i in range(m):
        for j in range(n):
            if j == 0:
                pass
            elif i == 0:
                dp[j] = dp[j - 1]
            else:
                dp[j] = min(dp[j - 1], dp[j])
            dp[j] += grid[i][j]
    return dp[n - 1]


if __name__ == '__main__':
    grid = [[1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]]

    print(min_path_sum(grid))  # 7
