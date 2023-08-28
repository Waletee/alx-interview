#!/usr/bin/python3

""" Finding perimeter of an island """

def island_perimeter(grid):
    """ Function that returns the perimieter of the island as described in grid """
    num_time = 0
    row = len(grid)
    col = len(grid[0]) if row else 0

    for a in range(len(grid)):
        for b in range(len(grid[a])):

            index = [(a - 1, b), (a, b - 1), (a, b + 1), (a + 1, b)]
            confirm = [1 if c[0] in range(row) and c[1] in range(col) else 0
                     for c in index]

            if grid[a][b]:
                num_time += sum([1 if not d or not grid[c[0]][c[1]] else 0
                              for d, c in zip(confirm, index)])

    return (num_time)
