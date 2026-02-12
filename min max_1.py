# Minimax function
def minimax(depth, nodeIndex, isMax, values, height):

    if depth == height:
        return values[nodeIndex]

    if isMax:
        return max(
            minimax(depth + 1, nodeIndex * 2, False, values, height),
            minimax(depth + 1, nodeIndex * 2 + 1, False, values, height)
        )
    else:
        return min(
            minimax(depth + 1, nodeIndex * 2, True, values, height),
            minimax(depth + 1, nodeIndex * 2 + 1, True, values, height)
        )


# Leaf node values from your diagram
values = [2, 3, 5, 9, 0, 1, 7, 5]

height = 3   # tree depth

result = minimax(0, 0, True, values, height)

print("Optimal value:", result)
