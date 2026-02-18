import itertools

dist=[[0,10,15,20],
      [10,0,35,25],
      [15,35,0,30],
      [20,25,30,0]]

cities=[0,1,2,3]
min_cost=999

for p in itertools.permutations(cities[1:]):
    cost=0
    k=0
    for j in p:
        cost+=dist[k][j]
        k=j
    cost+=dist[k][0]
    min_cost=min(min_cost,cost)

print("Minimum Cost:",min_cost)








