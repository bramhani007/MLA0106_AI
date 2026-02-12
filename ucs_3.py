import heapq

graph = {
    0: [(1,1)],
    1: [(3,1), (2,1)],
    2: [],
    3: [(4,1)],
    4: [(5,1)],
    5: [(7,1)],
    7: [(6,1)],
    6: [(4,1)]
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

ucs(0)
