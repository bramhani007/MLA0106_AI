from collections import deque

graph = {
    0: [1],
    1: [3, 2],
    2: [],
    3: [4],
    4: [5],
    5: [7],
    7: [6],
    6: [4]
}

def bfs(start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

    print("->".join(map(str, visited)))

bfs(0)
