from collections import deque

# Initial and Goal states
start = "123560784"
goal  = "123586074"

def print_board(state):
    print(state[0], state[1], state[2])
    print(state[3], state[4], state[5])
    print(state[6], state[7], state[8])
    print()

def get_moves(state):
    i = state.index('0')
    moves = []

    for j in [i-1, i+1, i-3, i+3]:
        if 0 <= j < 9:
            lst = list(state)
            lst[i], lst[j] = lst[j], lst[i]
            moves.append("".join(lst))

    return moves

def solve():
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            print("Step 1: Initial")
            print_board(path[0])

            step = 2
            for p in path[1:]:
                print("Step", step)
                print_board(p)
                step += 1
            return

        if state in visited:
            continue

        visited.add(state)

        for move in get_moves(state):
            queue.append((move, path + [move]))

solve()
