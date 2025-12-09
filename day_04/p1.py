with open("test.txt") as f:
    grid = [list(row) for row in [line.strip() for line in f.readlines()]]

# Goal: Find which marked cells have less than 4 neighbors
count = 0

def checkNeighbors(r, c):
    dirs = [(0, 1), (0,-1), (1,0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    neighborCount = 0
    for dr, dc in dirs:
        newR, newC = r + dr, c + dc
        if 0 <= newR < len(grid) and 0 <= newC < len(grid[0]) and grid[newR][newC] == "@":
            neighborCount += 1
        
    return neighborCount

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "@" and checkNeighbors(r, c) < 4:
            count += 1

print(grid)
        
print("Accessible Rolls of Paper:", count)