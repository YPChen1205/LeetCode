import collections


def find_redundant_connection(edges):
    """
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    graph = collections.defaultdict(set)

    def dfs(source, target):
        if source not in seen:
            seen.add(source)
            if source == target: return True
            return any(dfs(nei, target) for nei in graph[source])

    for u, v in edges:
        seen = set()
        if u in graph and v in graph and dfs(u, v):
            return u, v
        graph[u].add(v)
        graph[v].add(u)

if __name__ == "__main__":
    print(find_redundant_connection([[1,2], [1,3], [2,3]]))
    print(find_redundant_connection([[1,2], [2,3], [3,4], [1,4], [1,5]]))