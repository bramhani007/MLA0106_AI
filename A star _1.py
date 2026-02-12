import heapq

# Graph with costs
graph = {
    'S': [('A',3), ('D',4)],
    'A': [('B',4), ('D',5)],
    'B': [('C',4), ('E',5)],
    'C': [],
    'D': [('E',2)],
    'E': [('F',4)],
    'F': [('G',3.5)],
    'G': []
}

# Heuristic values
h = {
    'S':11.5, 'A':10.1, 'B':5.8, 'C':3.4,
    'D':9.2, 'E':7.1, 'F':3.5, 'G':0
}

def astar(start, goal):
    q = [(0, start, [start], 0)]   # (f, node, path, cost)

    while q:
        f, node, path, cost = heapq.heappop(q)

        if node == goal:
            print("Path:", "->".join(path))
            print("Cost:", cost)
            return

        for n, c in graph[node]:
            new_cost = cost + c
            new_f = new_cost + h[n]
            heapq.heappush(q, (new_f, n, path+[n], new_cost))

astar('S','G')
