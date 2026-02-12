import math

def ab(i, d, isMax, a, b):
    if d == 3:
        return v[i]

    if isMax:
        best = -math.inf
        best = max(best, ab(i*2, d+1, False, a, b))
        a = max(a, best)
        if b <= a: return best
        best = max(best, ab(i*2+1, d+1, False, a, b))
        return best
    else:
        best = math.inf
        best = min(best, ab(i*2, d+1, True, a, b))
        b = min(b, best)
        if b <= a: return best
        best = min(best, ab(i*2+1, d+1, True, a, b))
        return best

# Leaf node values from your tree
v = [2, 3, 5, 9, 0, 1, 7, 5]

result = ab(0, 0, True, -math.inf, math.inf)

print("Optimal value:", result)
