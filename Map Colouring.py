colors = ["Red","Green","Blue"]

states = ['A','B','C','D']

graph = {
 'A':['B','C'],
 'B':['A','C','D'],
 'C':['A','B','D'],
 'D':['B','C']
}

result = {}

def safe(state,color):
    for n in graph[state]:
        if n in result and result[n]==color:
            return False
    return True

def solve(i):
    if i==len(states):
        print(result)
        return True
    state=states[i]
    for color in colors:
        if safe(state,color):
            result[state]=color
            if solve(i+1):
                return True
            result.pop(state)

solve(0)
