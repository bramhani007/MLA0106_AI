import heapq

# Heuristic values
h = {
    'A': 40,
    'B': 32,
    'C': 25,
    'D': 35,
    'E': 19,
    'F': 17,
    'H': 10,
    'G': 0
}

# Graph connections
graph = {
    'A': ['C', 'D', 'B'],
    'B': ['E'],
    'C': ['F', 'E'],
    'D': ['F'],
    'E': ['H'],
    'F': ['G'],
    'H': ['G'],
    'G': []
}

def greedy_bfs(start, goal):
    visited = []
    pq = [(h[start], start)]

    while pq:
        _, node = heapq.heappop(pq)

        if node not in visited:
            visited.append(node)

            if node == goal:
                break

            for neigh in graph[node]:
                heapq.heappush(pq, (h[neigh], neigh))

    print("->".join(visited))

greedy_bfs('A', 'G')
