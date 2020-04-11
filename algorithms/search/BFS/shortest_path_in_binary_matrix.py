def shortest_path_binary_matrix(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    if grid is None or len(grid) == 0 or len(grid[0]) == 0:
        return -1

    directions = [[1, 1], [1, -1], [1, 0], [0, 1], [0, -1], [-1, 0], [-1, 1], [-1, -1]]
    m = len(grid)
    n = len(grid[0])
    queue = [[0, 0]]
    path_len = 0

    while queue:
        queue_len = len(queue)
        path_len += 1

        while queue_len > 0:
            cur = queue[0]
            queue.pop(0)
            queue_len -= 1

            cr = cur[0]
            cc = cur[1]
            if grid[cr][cc] == 1:
                continue
            if cr == m - 1 and cc == n - 1:
                return path_len
            grid[cc][cr] = 1
            for d in directions:
                nr = cr + d[0]
                nc = cc + d[1]
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                queue.append([nr, nc])
    return -1


if __name__ == '__main__':
    print(shortest_path_binary_matrix([[0,1],[1,0]]))
    print(shortest_path_binary_matrix([[0,0,0],[1,1,0],[1,1,0]]))
