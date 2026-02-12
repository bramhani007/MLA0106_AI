graph = {
    1: [2, 7],
    2: [3, 6],
    3: [4, 5],
    4: [],
    5: [],
    6: [],
    7: [8, 10],
    8: [9],
    9: [],
    10: []
}

visited = []

def dfs(node):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(n)

dfs(1)
print("->".join(map(str, visited)))
