from functools import lru_cache

with open("input.txt") as f:
    data = f.read().strip().splitlines()
grid = tuple(data)

@lru_cache()
def count_timelines(row, col):
    # Base case: reached bottom of grid = 1 complete timeline
    if row >= len(grid):
        return 1
    
    cell = grid[row][col]
    
    if cell == "^":
        # Split beam; count paths going left + paths going right
        timelines = 0
        if col - 1 >= 0:
            timelines += count_timelines(row + 1, col - 1)
        if col + 1 < len(grid[0]):
            timelines += count_timelines(row + 1, col + 1)
        return timelines
    else:
        # Continue straight down; same case for "S", "."", and "|"
        return count_timelines(row + 1, col)

# Find starting column
start_col = next(c for c in range(len(grid[0])) if grid[0][c] == "S")

total_timelines = count_timelines(0, start_col)
print("Total number of timelines:", total_timelines)