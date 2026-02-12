import heapq

# Graph with costs
graph = {
    'S': [('A',3), ('D',2)],
    'A': [('B',5), ('C',10)],
    'B': [('C',2), ('E',1)],
    'C': [('G',4)],
    'D': [('E',4), ('B',1)],
    'E': [('G',3)],
    'G': []
}

# Heuristic values
h = {
    'S':7, 'A':9, 'B':4,
    'C':2, 'D':5, 'E':3, 'G':0
}

def astar(start, goal):
    q = [(0, start, [start], 0)]  # (f, node, path, cost)

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
