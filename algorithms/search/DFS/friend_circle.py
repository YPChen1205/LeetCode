def find_circle_num(M):
    """
    :type M: List[List[int]]
    :rtype: int
    """
    n = len(M)
    circle_num = 0
    visited = [False for i in range(n)]
    for i in range(n):
        if visited[i]:
            continue
        dfs(M, i, visited)
        circle_num += 1
    return circle_num


def dfs(M, i, visited):
    visited[i] = True
    for j in range(len(M)):
        if M[i][j] == 1 and not visited[j]:
            dfs(M, j, visited)


if __name__ == '__main__':
    print(find_circle_num([[1,1,0],[1,1,0],[0,0,1]]))