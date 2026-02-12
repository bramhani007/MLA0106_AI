import heapq

graph = {
    1: [(2,1), (3,1)],
    2: [(5,1), (6,1)],
    3: [(4,1), (7,1)],
    4: [(8,1)],
    5: [],
    6: [],
    7: [(8,1)],
    8: []
}

def ucs(start):
    visited = []
    pq = [(0, start)]

    while pq:
        cost, node = heapq.heappop(pq)

        if node not in visited:
            visited.append(node)
            for neigh, w in graph[node]:
                heapq.heappush(pq, (cost + w, neigh))

    print("->".join(map(str, visited)))

ucs(1)
