"""
idea comes from  "Huahua's Tech Road"
"""
def can_finish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    neighbors = {}

    for i in range(numCourses):
        neighbors[i] = []
    for e in prerequisites:
        neighbors[e[1]].append(e[0])

    status = [0 for i in range(numCourses)]  # nodes status( 0: unvisited, 1: visiting 2:visited)

    for i in range(numCourses):
        if dfs(i, status, neighbors):
            return False
    return True

def find_order(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """
    neighbors = {}
    order = []
    for i in range(numCourses):
        neighbors[i] = []
    for e in prerequisites:
        neighbors[e[1]].append(e[0])

    status = [0 for i in range(numCourses)]  # nodes status( 0: unvisited, 1: visiting 2:visited)

    for i in range(numCourses):
        if dfs_keep_order(i, status, neighbors, order):
            return False
    order.reverse()
    return order

def dfs(cur, status, neighbors):
    if status[cur] == 1:
        return True
    if status[cur] == 2:
        return False

    status[cur] = 1
    for n in neighbors[cur]:
       if dfs(n, status, neighbors):
           return True

    status[cur] = 2
    return False


def dfs_keep_order(cur, status, neighbors, order):
    if status[cur] == 1:
        return True
    if status[cur] == 2:
        return False

    status[cur] = 1
    for n in neighbors[cur]:
       if dfs_keep_order(n, status, neighbors,order):
           return True

    status[cur] = 2
    order.append(cur)

    return False



if __name__ == "__main__":
    print(can_finish(2,[[0,1]]))
    print(can_finish(2,[[0,1],[1,0]]))
    print(find_order(2,[[1,0]]))
    print(find_order(4,[[1,0],[2,0],[3,1],[3,2]]))

