class Solution(object):
    def __init__(self):
        self.m = 0
        self.n = 0
        self.matrix = []
        self.direction = [[0, -1], [0, 1], [-1, 0], [1, 0]]

    def pacific_atlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        if not (matrix and len(matrix)):
            return res

        self.m = len(matrix)
        self.n = len(matrix[0])
        self.matrix = matrix
        reach_P = [[False for j in range(self.n)] for i in range(self.m)]
        reach_A = [[False for j in range(self.n)] for i in range(self.m)]

        for i in range(self.m):
            self.dfs(i, 0, reach_P)
            self.dfs(i, self.n - 1, reach_A)

        for j in range(self.n):
            self.dfs(0, j, reach_P)
            self.dfs(self.m - 1, j, reach_A)

        for i in range(self.m):
            for j in range(self.n):
                if reach_P[i][j] and reach_A[i][j]:
                    res.append([i, j])
        print(reach_P)
        print(reach_A)
        return res

    def dfs(self, i, j, reach):
        if reach[i][j]:
            return
        reach[i][j] = True
        for d in self.direction:
            next_i = i + d[0]
            next_j = j + d[1]
            if not (0 <= next_i < self.m and 0 <= next_j < self.n and self.matrix[i][j] >= self.matrix[next_i][next_j]):
                continue
            self.dfs(next_i, next_j, reach)


if __name__ == '__main__':
    sol = Solution()
    print(sol.pacific_atlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
