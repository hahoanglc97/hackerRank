class nodeX:
    def __init__(self, name):
        self.name = name
        self.connections = {}


def prims(n, edges, start):
    graph = {}
    for i in edges:
        x, y, r = i
        if x not in graph:
            graph[x] = nodeX(x)
        if y not in graph:
            graph[y] = nodeX(y)

        graph[x].connections[graph[y]] = r
        graph[y].connections[graph[x]] = r
    visited = {graph[start]: 0}
    while len(visited) != n:
        lowestCost = (None, float('inf'))
        for node in visited:
            for nextNode, weight in node.connections.items():
                if nextNode not in visited and weight < lowestCost[1]:
                    lowestCost = (nextNode, weight)
        node, weight = lowestCost
        visited[node] = weight
    print(sum(visited.values()))

edges = [[1, 2, 3], [1, 3, 4], [4, 2, 6], [5, 2, 2], [2, 3, 5], [3, 5, 7]]
result = prims(5, edges, 1)