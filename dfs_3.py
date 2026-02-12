graph = {
    0: [1],
    1: [3, 2],
    2: [],
    3: [4],
    4: [5],
    5: [7],
    7: [6],
    6: [4]
}

visited = []

def dfs(node):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(n)

dfs(0)
print("->".join(map(str, visited)))
