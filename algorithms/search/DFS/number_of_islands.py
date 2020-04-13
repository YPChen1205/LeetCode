class Solution(object):
    def __init__(self):
        self.directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        self.m = 0
        self.n = 0

    def num_islands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.m = len(grid)
        self.n = len(grid[0])
        if not (grid and self.m and self.n):
            return 0
        islands_num = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    islands_num += 1
        return islands_num

    def dfs(self, grid, i, j):
        if not (0 <= i < self.m and 0 <= j < self.n):
            return
        grid[i][j] = '0'
        for d in self.directions:
            self.dfs(grid, i + d[0], j + d[1])


if __name__ == '__main__':
    sol = Solution()
    print(sol.num_islands(
        [['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]))
