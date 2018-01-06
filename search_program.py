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
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1
heuristic_cost = len(grid)-1 + len(grid[0])-1

delta = [[-1, 0, 'v'], # go up
         [ 0,-1, '>'], # go left
         [ 1, 0, '^'], # go down
         [ 0, 1, '<']] # go right

new_delta = [[ 1, 0, '^'], # go down
             [ 0, 1, '<'], # go right
             [-1, 0, 'v'], # go up
             [ 0,-1, '>']] # go left


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

heuristic_grid = np.array(grid)
heuristic_grid[heuristic_grid > -1] = -1

path_grid = np.empty((len(grid), len(grid[0])), dtype='str')
path_grid[:] = ' '

expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]

expansion_counter = 0
def update_expansion_grid(place):
    global expansion_counter
    expansion_grid[place[0], place[1]] = expansion_counter
    expansion_counter += 1

def is_in_grid(new_place):
    if (new_place[0] > len(grid)-1 or
        new_place[0] < 0 or
        new_place[1] > len(grid[0])-1 or
        new_place[1] < 0 or
        grid[new_place[0]][new_place[1]] == 1 ):
        return 0
    return 1

def find_pre(cost, current):
    for direction in delta:
        new_place = [current[0] + direction[0], current[1] + direction[1]]
        if (is_in_grid(new_place)):
            if (cost_grid[new_place[0], new_place[1]] == cost - 1):
                return new_place, direction[2]
    return 0,0

def calc_path(cost):
    new_place = [goal[0], goal[1]]
    path_grid[goal[0], goal[1]] = '*'
    while (cost > -1):
        new_place, sign = find_pre(cost, new_place)
        if sign == 0:
            return
        path_grid[new_place[0], new_place[1]] = sign
        cost -=1

def is_in_grid_heuristic(new_place):
    if (new_place[0] > len(grid)-1 or
        new_place[0] < 0 or
        new_place[1] > len(grid[0])-1 or
        new_place[1] < 0 or
        grid[new_place[0]][new_place[1]] == 1 or
        heuristic_grid[new_place[0]][new_place[1]] > -1):
        return 0
    return 1

heuristic_counter = 1
def calc_heuristic(round):
    global heuristic_counter
    next_round = []
    for start in round:
        for direction in new_delta:
            if (heuristic_grid[goal[0], goal[1]] > -1):
                return
            new_place = [start[0] + direction[0], start[1] + direction[1]]
            if (is_in_grid_heuristic(new_place)):
                heuristic_grid[new_place[0], new_place[1]] = heuristic_counter
                heuristic_counter += 1
                calc_heuristic([new_place])
                #update_expansion_grid(new_place)
    return next_round


def search(grid,init,goal,cost):
    start = [0,0]
    update_expansion_grid(start)

    # Regular search - building the cost and expansion grids
    next_round = [start]
    while (len(next_round) > 0):
        next_round = calc_cost(next_round)

    # A* search
    next_round = [start]
    heuristic_grid[0,0] = 0
    calc_heuristic(next_round)

    final_cost = cost_grid[goal[0], goal[1]]
    calc_path(final_cost)

    print("original grid:")
    print(grid)
    print("cost grid:")
    print(cost_grid)
    print("expansion grid:")
    print(expansion_grid)
    print("path grid:")
    print (path_grid)
    print("heuristic grid:")
    print (heuristic_grid)

    if final_cost == 0:
        return 'fail'
    return [cost_grid[goal[0], goal[1]], goal[0], goal[1]]

path = search(grid,init,goal,cost)
print("result:" , path)