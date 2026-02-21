# A* SEARCH FOR 8-PUZZLE
# Heuristics:
# H1 -> Misplaced Tiles
# H2 -> Manhattan Distance

import heapq

GOAL_STATE = (1,2,3,
              4,5,6,
              7,8,0)

GOAL_POS = {value:(i//3, i%3) for i, value in enumerate(GOAL_STATE)}

# Heuristic 1: Misplaced Tiles
def h1_misplaced(state):
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != GOAL_STATE[i]:
            count += 1
    return count

# Heuristic 2: Manhattan Distance
def h2_manhattan(state):
    dist = 0
    for i, value in enumerate(state):
        if value == 0:
            continue
        r, c = i//3, i%3
        gr, gc = GOAL_POS[value]
        dist += abs(r-gr) + abs(c-gc)
    return dist


def get_neighbors(state):
    neighbors = []
    idx = state.index(0)
    r, c = idx//3, idx%3

    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    for dr, dc in moves:
        nr, nc = r+dr, c+dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_idx = nr*3 + nc
            new_state = list(state)
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            neighbors.append(tuple(new_state))

    return neighbors


def astar(start, heuristic):

    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_cost = {start:0}
    explored_nodes = 0

    while open_list:
        _, current = heapq.heappop(open_list)
        explored_nodes += 1

        if current == GOAL_STATE:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, explored_nodes

        for neighbor in get_neighbors(current):
            tentative_g = g_cost[current] + 1

            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                came_from[neighbor] = current
                g_cost[neighbor] = tentative_g
                f = tentative_g + heuristic(neighbor)
                heapq.heappush(open_list, (f, neighbor))

    return None, explored_nodes


def print_state(state):
    for i in range(0,9,3):
        print(state[i:i+3])
    print()


def get_user_input():
    print("\nEnter 8-Puzzle Initial State (use 0 for blank)")
    print("Enter numbers row-wise separated by space")
    print("Example: 1 2 3 4 0 6 7 5 8")

    while True:
        data = input("Enter 9 numbers: ").split()

        if len(data) != 9:
            print("Invalid input. Enter exactly 9 numbers.")
            continue

        nums = tuple(map(int, data))

        if sorted(nums) != list(range(9)):
            print("Numbers must be from 0 to 8 without repetition.")
            continue

        return nums


if __name__ == "__main__":

    START_STATE = get_user_input()

    print("\n========== USING H1 (MISPLACED TILES) ==========")
    path1, nodes1 = astar(START_STATE, h1_misplaced)

    if path1:
        for step in path1:
            print_state(step)
        print("Solution Depth:", len(path1)-1)
        print("Nodes Explored:", nodes1)
    else:
        print("No Solution Found")


    print("\n========== USING H2 (MANHATTAN DISTANCE) ==========")
    path2, nodes2 = astar(START_STATE, h2_manhattan)

    if path2:
        for step in path2:
            print_state(step)
        print("Solution Depth:", len(path2)-1)
        print("Nodes Explored:", nodes2)
    else:
        print("No Solution Found")


    print("\n========== PERFORMANCE COMPARISON ==========")
    print("H1 -> Nodes:", nodes1, ", Depth:", len(path1)-1 if path1 else 0)
    print("H2 -> Nodes:", nodes2, ", Depth:", len(path2)-1 if path2 else 0)
