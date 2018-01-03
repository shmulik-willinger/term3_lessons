# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space
import numpy as np

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def is_possible(new_place):
    if (new_place[0] > grid.__len__()-1 or
        new_place[0] < 0 or
        new_place[1] > grid[0].__len__()-1 or
        new_place[1] < 0 or
        cost_grid[new_place[0], new_place[1]] > 0 or
        grid[new_place[0]][new_place[1]] == 1 or
        new_place == [0,0]):
        return 0
    return 1


def calc_cost(round):
    next_round = []
    for start in round:
        for direction in delta:
            new_place = [start[0] + direction[0], start[1] + direction[1]]
            if (is_possible(new_place)):
                cost_grid[new_place[0], new_place[1]] = cost_grid[start[0], start[1]]+1
                next_round += [new_place]
                update_expansion_grid(new_place)
    return next_round

cost_grid = np.array(grid)
cost_grid[cost_grid > 0] = 0

expansion_grid = np.array(grid)
expansion_grid[expansion_grid > -1] = -1

expansion_counter = 0
def update_expansion_grid(place):
    global expansion_counter
    expansion_grid[place[0], place[1]] = expansion_counter
    expansion_counter += 1

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    start = [0,0]
    next_round = [start]
    update_expansion_grid(start)

    while (len(next_round) > 0):
        next_round = calc_cost(next_round)

    #print(cost_grid)
    print(expansion_grid)

    final_cost = cost_grid[goal[0], goal[1]]
    if final_cost == 0:
        return 'fail'
    return [cost_grid[goal[0], goal[1]], goal[0], goal[1]]

path = search(grid,init,goal,cost)
print(path)