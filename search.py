# ----------
# User Instructions:
#
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal.
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------
import numpy as np

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1  # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0, 'v'], # go up
         [ 0,-1, '>'], # go left
         [ 1, 0, '^'], # go down
         [ 0, 1, '<']] # go right

delta_name = ['^', '<', 'v', '>']

def is_possible_cell(cell, cost_grid):
    if (cell[0] > len(grid)-1 or
        cell[0] < 0 or
        cell[1] > len(grid[0])-1 or
        cell[1] < 0 or
        cost_grid[cell[0]][cell[1]] > 0 or
        cell == goal):
        return 0
    return 1

def update_value(cost_grid, path_grid, next_cell):
    current_cells = []
    for cell in next_cell:
        for side in delta:
            current = [cell[0] + side[0], cell[1] + side[1]]
            if is_possible_cell(current, cost_grid):
                cost_grid[current[0], current[1]] = cost_grid[cell[0], cell[1]] +1
                path_grid[current[0], current[1]] = side[2]
                current_cells.append((current))
    return current_cells


def compute_value(grid, goal, cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    cost_grid = np.array(grid)
    cost_grid[cost_grid > 0] = 99

    path_grid = np.empty((len(grid), len(grid[0])), dtype='str')
    path_grid[:] = ' '

    next_cell = [goal]
    path_grid[goal[0], goal[1]] = '*'
    while(len(next_cell) > 0):
        next_cell = update_value(cost_grid, path_grid, next_cell)

    # make sure your function returns a grid of values as
    # demonstrated in the previous video.
    return cost_grid, path_grid

cost_grid, path_grid = compute_value(grid, goal, cost)
print(cost_grid)
print(path_grid)