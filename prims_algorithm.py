class node:
    def __init__(self, name):
        self.name = name
        self.connections = {}


n, m = list(map(int, input().strip().split()))

# Build graph
graph = {}
for i in range(m):
    x, y, r = list(map(int, input().strip().split()))

    # Add the two nodes if they're not already in the graph
    if x not in graph:
        graph[x] = node(x)
    if y not in graph:
        graph[y] = node(y)

    # Connect the two nodes
    graph[x].connections[graph[y]] = r
    graph[y].connections[graph[x]] = r

# Add starting node to visited list
s = int(input().strip())
visited = {graph[s]: 0}

# Perform Prim's algorithm on graph
while len(visited) != n:
    lowestCost = (None, float('inf'))
    for node in visited:
        for nextNode, weight in node.connections.items():
            if nextNode not in visited and weight < lowestCost[1]:
                lowestCost = (nextNode, weight)

    node, weight = lowestCost
    visited[node] = weight

# Print out sum of weights (aka cost of the MST)
print(sum(visited.values()))

# edges = [[1, 2, 3], [1, 3, 4], [4, 2, 6], [5, 2, 2], [2, 3, 5], [3, 5, 7]]
# result = prims(5, edges, 1)
# print(result)
