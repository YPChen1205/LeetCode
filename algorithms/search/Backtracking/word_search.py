def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    m = len(board)
    n = len(board[0])
    visited = [[False for j in range(n)] for i in range(m)]
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def backtrack(idx, r, c, visited, board, word):
        if idx == len(word):
            return True
        if not (0 <= r < m and 0 <= c < n) or visited[r][c] or board[r][c] != word[idx]:
            return False

        visited[r][c] = True

        for d in directions:
            if backtrack(idx + 1, r + d[0], c + d[1], visited, board, word):
                return True
        visited[r][c] = False
        return False

    for r in range(m):
        for c in range(n):
            if backtrack(0, r, c, visited, board, word):
                return True
    return False


if __name__ == '__main__':
    board = [['A', 'B', 'C', 'E'],
             ['S', 'F', 'C', 'S'],
             ['A', 'D', 'E', 'E']]

    # print(exist(board, "ABCCED"))
    print(exist(board, "SEE"))
    # print(exist(board, "ABCB"))
