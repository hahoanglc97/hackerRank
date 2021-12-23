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
    return sum(visited.values())

if __name__ == '__main__':
    fptr = open('test_case/primsmstsub-testcases.txt', 'r')
    count = 0
    edges = []
    n = 0
    m = 0
    start = 0
    result = 0
    while True:
        count += 1

        # Get next line from file
        line = fptr.readline()

        # if line is empty
        # end of file is reached
        if not line:
            break

        if count == 1:
            n, k, start, result = list(map(int, line.rstrip().split()))
        else:
            contentLine = list(map(int, line.rstrip().split()))
            edges.append(contentLine)

    print('{:15} : {}'.format('Output', prims(n, edges, start)))
    print('{:15} : {}'.format('Expected Output', result))

    fptr.close()
