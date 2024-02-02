def is_valid_state(state):
    missionaries, cannibals, boat = state

    # Check if the number of missionaries is greater than or equal to cannibals
    if missionaries < 0 or cannibals < 0 or missionaries > 3 or cannibals > 3:
        return False

    # Check if missionaries are outnumbered by cannibals on either side
    if missionaries < cannibals and missionaries > 0:
        return False

    # Check if the state is valid on both sides of the river
    missionaries_on_other_side = 3 - missionaries
    cannibals_on_other_side = 3 - cannibals

    if missionaries_on_other_side < cannibals_on_other_side and missionaries_on_other_side > 0:
        return False

    return True

def is_goal_state(state):
    return state == (0, 0, 0)

def get_next_states(current_state):
    possible_moves = [
        (1, 0),  # Move one missionary
        (2, 0),  # Move two missionaries
        (0, 1),  # Move one cannibal
        (0, 2),  # Move two cannibals
        (1, 1)   # Move one missionary and one cannibal
    ]

    current_m, current_c, current_b = current_state
    next_states = []

    for move in possible_moves:
        move_m, move_c = move

        if current_b == 1:
            next_state = (current_m - move_m, current_c - move_c, 0)
        else:
            next_state = (current_m + move_m, current_c + move_c, 1)

        if is_valid_state(next_state):
            next_states.append(next_state)

    return next_states

def dfs(current_state, visited_states):
    visited_states.add(current_state)

    if is_goal_state(current_state):
        return [current_state]

    for next_state in get_next_states(current_state):
        if next_state not in visited_states:
            path = dfs(next_state, visited_states)
            if path:
                return [current_state] + path

    return None

def solve_missionaries_and_cannibals():
    initial_state = (3, 3, 1)
    visited_states = set()

    solution_path = dfs(initial_state, visited_states)

    if solution_path:
        print("Solution found:")
        for state in solution_path:
            print(state)
    else:
        print("No solution found.")

# Run the solver
solve_missionaries_and_cannibals()