with open("input.txt") as f:
    grid = [list(row) for row in [line.strip() for line in f.readlines()]]

# Goal: Find how many rolls can be accessed

# Steps:
# - Find which marked cells have less than 4 neighbors
# - Add cells to count, then remove them (mark as empty)
# - Keep doing the above steps until no more rolls can be accessed

def countNeighbors(r, c):
    dirs = [(0, 1), (0,-1), (1,0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    neighborCount = 0
    for dr, dc in dirs:
        newR, newC = r + dr, c + dc
        if 0 <= newR < len(grid) and 0 <= newC < len(grid[0]) and grid[newR][newC] == "@":
            neighborCount += 1
        
    return neighborCount

count = 0

while True:
    curCount = 0
    toRemove = []
    
    # find which rolls can be accessed
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "@" and countNeighbors(r, c) < 4:
                toRemove.append((r, c))
                
    if len(toRemove) == 0:
        break # no more rolls can be accessed, exit loop
    else:
        for r, c in toRemove:
            curCount += 1
            grid[r][c] = "."
            
    print("Rolls Accessed This Iteration:", curCount)
    count += curCount

print("Accessible Rolls of Paper:", count)