def surronded_region(board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    if not (board and len(board)):
        return
    n = len(board)
    m = len(board[0])
    visited = [[False for j in range(m)] for i in range(n)]

    # define the border area
    border = set()
    for i in range(n):
        border.add((i, 0))
        border.add((i, n - 1))
    for j in range(m):
        border.add((0, j))
        border.add((m - 1, j))

    for i, j in border:
        dfs(board, visited, i, j)

    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                board[i][j] = 'X'
    return board


def dfs(board, visited, i, j):
    if not (0 <= i < len(board) and 0 <= j < len(board[0])) or board[i][j] == 'X' or visited[i][j]:
        return
    visited[i][j] = True
    dfs(board, visited, i - 1, j)
    dfs(board, visited, i + 1, j)
    dfs(board, visited, i, j - 1)
    dfs(board, visited, i, j + 1)


if __name__ == '__main__':
    print(surronded_region([['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]))
