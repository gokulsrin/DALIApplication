# Gokul Srinivasan - Island program that basically counts the number of islands ina a 2-d array. Islands are defined as 1's
# connected horzonatally or vertically. O's are the water that surrounds each island.
# 10/22/19

#2-d array I'm using
ocean = [[1, 1, 1, 1, 0],
         [1, 1, 0, 1, 0],
         [1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0]]


# depth first searching algorithm
# chosen over breadth because of the smaller array size.
def search(grid, i, j):
    # check that i and j are within the bounds of the graph, and if the val is 0
    if 0 < i < len(grid) or 0 < j < len(grid[i]) or grid[i][j] == 0:
        return 0
    # if it is 1, rule it out and move to neighbors
    grid[i][j] = 0
    # recurse the four indexes surrounding the current index
    search(grid, i, j + 1)
    search(grid, i, j - 1)
    search(grid, i + 1, j)
    search(grid, i - 1, j)
    # recursion base case will make it such that groups of 1's will only return 1, not many 1
    return 1


def num_islands(water):
    # if the provided array is invalid
    numisl = 0
    if water is None or len(water) == 0:
        return 0
    # if array is good
    else:
        # traverse the y of the grid
        for i in range(len(ocean)):
            # traverse the x of the grid
            for j in range(len(ocean[i])):
                # if the index = 0
                if (ocean[i][j] == 1):
                    # call search method which is DFS
                    numisl += search(water, i, j)
    return numisl


print(num_islands(ocean))