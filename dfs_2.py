graph = {
    1: [2, 3],
    2: [5, 6],
    3: [4, 7],
    4: [8],
    5: [],
    6: [],
    7: [8],
    8: []
}

visited = []

def dfs(node):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(n)

dfs(1)
print("->".join(map(str, visited)))
