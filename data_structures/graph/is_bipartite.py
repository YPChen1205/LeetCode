"""
Idea: convert it to 2-color problem Edge(x,j) -> [color(x) = 1 - color(y)]
"""

def is_bipartite(graph):
    """
    :type graph: List[List[int]]
    :rtype: bool
    """
    nodes = range(len(graph))

    color = [-1 for i in nodes] # -1 mean node i isn't colored yet
    color[0] = 0 # assign the first node with color 0

    for i in nodes:
        for j in graph[i]:
            if color[j] == -1:
                color[j] = 1-color[i]
            elif color[j] != 1-color[i]:
                return False
    return True


if __name__ == "__main__":
    print(is_bipartite([[1,3], [0,2], [1,3], [0,2]]))
    print(is_bipartite([[1,2,3], [0,2], [0,1,3], [0,2]]))
