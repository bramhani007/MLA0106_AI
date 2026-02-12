import heapq

# Graph with costs
graph = {
    'A': [('B',1), ('C',4)],
    'B': [('C',2), ('D',3)],
    'C': [('E',3)],
    'D': [('F',2), ('G',4)],
    'E': [('G',3)],
    'F': [('G',1)],
    'G': []
}

# Heuristic values
h = {
    'A':7, 'B':6, 'C':4,
    'D':3, 'E':3, 'F':1, 'G':0
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

astar('A','G')
