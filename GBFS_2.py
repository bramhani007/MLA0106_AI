import heapq

# Heuristic values
h = {
    'P': 10,
    'R': 8,
    'C': 6,
    'A': 11,
    'M': 9,
    'L': 9,
    'U': 4,
    'N': 6,
    'E': 3,
    'S': 0
}

# Graph connections
graph = {
    'P': ['R', 'C', 'A'],
    'C': ['R', 'U', 'M'],
    'R': ['E'],
    'A': ['M'],
    'M': ['L', 'U'],
    'L': ['N'],
    'U': ['S', 'N'],
    'N': ['S'],
    'E': ['S'],
    'S': []
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

greedy_bfs('P', 'S')
