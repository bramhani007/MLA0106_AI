from collections import deque

start = (3,3,1)
goal = (0,0,0)

def valid(m,c):
    return (m==0 or m>=c) and (3-m==0 or 3-m>=3-c)

def print_state(m,c,b):
    left_m = 'M '*m
    left_c = 'C '*c
    right_m = 'M '*(3-m)
    right_c = 'C '*(3-c)

    if b==1:
        boat = "<-B->"
    else:
        boat = "<-B->"

    print("Left Side :", left_m, left_c)
    print("           ", boat)
    print("Right Side:", right_m, right_c)
    print("----------------------")

def solve():
    q = deque([(start,[start])])
    visited = set()

    while q:
        (m,c,b), path = q.popleft()

        if (m,c,b) == goal:
            print("Initial State")
            for state in path:
                print_state(state[0],state[1],state[2])
            print("Goal Reached")
            return

        if (m,c,b) in visited:
            continue

        visited.add((m,c,b))

        for dm,dc in [(1,0),(2,0),(0,1),(0,2),(1,1)]:
            if b==1:
                nm,nc = m-dm,c-dc
            else:
                nm,nc = m+dm,c+dc

            if 0<=nm<=3 and 0<=nc<=3 and valid(nm,nc):
                q.append(((nm,nc,1-b), path+[(nm,nc,1-b)]))

solve()
