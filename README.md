# MLA0106_AI
Artificial Intelligence Lab Programs – Python  :  Collection of basic AI programs implemented in Python.  Includes:  BFS, DFS, UCS, A* Search, Greedy Search ,Minimax, Alpha–Beta Pruning ,8 Puzzle, Water Jug, Missionaries &amp; Cannibals ,8 Queens, Map Coloring ,Decision Tree, Neural Network

1) 8–Puzzle (BFS)

   START
Read start_state, goal_state
Create QUEUE and VISITED set
Push start_state into QUEUE
WHILE QUEUE not empty:
    state ← pop front
    IF state = goal_state: STOP
    Generate all valid moves
    FOR each new_state:
        IF not visited:
            Mark visited
            Push into QUEUE
END

