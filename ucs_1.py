import heapq

graph = {
    1: [(2,1), (3,1)],
    2: [(4,1), (5,1)],
    3: [],
    4: [],
    5: []
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
