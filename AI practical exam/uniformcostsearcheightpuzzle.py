from queue import PriorityQueue

# Function to check if the puzzle is solved
def is_goal(state):
    goal_state = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 0]]
    return state == goal_state

# Function to find the possible moves
def possible_moves(state):
    moves = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                if i > 0:
                    moves.append((i, j, i - 1, j))
                if i < 2:
                    moves.append((i, j, i + 1, j))
                if j > 0:
                    moves.append((i, j, i, j - 1))
                if j < 2:
                    moves.append((i, j, i, j + 1))
    return moves

# Function to apply a move to the state
def apply_move(state, move):
    new_state = [row[:] for row in state]
    i, j, new_i, new_j = move
    new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
    return new_state

# Function for uniform cost search
def ucs(start_state):
    queue = PriorityQueue()
    queue.put((0, start_state, []))  # (cost, state, path)
    visited = set()
    while not queue.empty():
        cost, current_state, path = queue.get()
        if is_goal(current_state):
            return path
        if tuple(map(tuple, current_state)) not in visited:
            visited.add(tuple(map(tuple, current_state)))
            for move in possible_moves(current_state):
                new_state = apply_move(current_state, move)
                new_cost = cost + 1
                new_path = path + [move]
                queue.put((new_cost, new_state, new_path))
    return None

# Function to print the puzzle state
def print_puzzle(state):
    for row in state:
        print(row)

# Example usage
if __name__ == "__main__":
    initial_state = [[1, 2, 3],
                     [0, 4, 6],
                     [7, 5, 8]]
    print("Start State:")
    print_puzzle(initial_state)
    print("\nSolving...")
    solution = ucs(initial_state)
    if solution:
        print("\nFound solution")
        step = 1
        current_state = initial_state
        for move in solution:
            print("\nStep {}:".format(step))
            step += 1
            current_state = apply_move(current_state, move)
            print_puzzle(current_state)
    else:
        print("No solution found.")
