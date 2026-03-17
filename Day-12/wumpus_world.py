# Wumpus World game simulation with random hazards and manual agent movement

import random

SIZE = 4

grid = [["" for _ in range(SIZE)] for _ in range(SIZE)]

agent_x, agent_y = 0, 0

def random_position():
    while True:
        x = random.randint(0, SIZE-1)
        y = random.randint(0, SIZE-1)
        if (x, y) != (0,0) and grid[x][y] == "":
            return x, y

wx, wy = random_position()
grid[wx][wy] = "W"

gx, gy = random_position()
grid[gx][gy] = "G"

for _ in range(3):
    px, py = random_position()
    grid[px][py] = "P"

def percepts(x, y):
    breeze = False
    stench = False
    glitter = False

    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < SIZE and 0 <= ny < SIZE:
            if grid[nx][ny] == "P":
                breeze = True
            if grid[nx][ny] == "W":
                stench = True

    if grid[x][y] == "G":
        glitter = True

    return breeze, stench, glitter

while True:

    print("\nAgent Position:", (agent_x+1, agent_y+1))

    breeze, stench, glitter = percepts(agent_x, agent_y)

    print("Breeze detected!" if breeze else "No Breeze")
    print("Stench detected!" if stench else "No Stench")

    if glitter:
        print("Glitter detected! Gold found.")
        print("Agent wins!")
        break

    if grid[agent_x][agent_y] == "P":
        print("Agent fell into a Pit. Game Over.")
        break

    if grid[agent_x][agent_y] == "W":
        print("Agent eaten by Wumpus. Game Over.")
        break

    print("\nMove Options")
    print("1. Move Up")
    print("2. Move Down")
    print("3. Move Left")
    print("4. Move Right")

    move = int(input("Enter move: "))

    if move == 1 and agent_x > 0:
        agent_x -= 1
    elif move == 2 and agent_x < SIZE-1:
        agent_x += 1
    elif move == 3 and agent_y > 0:
        agent_y -= 1
    elif move == 4 and agent_y < SIZE-1:
        agent_y += 1
    else:
        print("Invalid move or boundary reached")
