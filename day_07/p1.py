from collections import defaultdict

with open("input.txt") as f:
    data = f.read().strip().splitlines()

data = [list(line) for line in data]
splitCount = 0
    
# Go line-by-line, find occurences of "^", check if cell above is "|", increase count and propogate "|" to left and right sides
# Bounds checks will be very important here

# We're pretty much just counting the amount of times a "|" is above a "^"

for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r][c] == "S":
            data[r+1][c] = "|"
        elif data[r][c] == "^":
            if data[r-1][c] == "|":
                splitCount += 1
                # Propogate left
                left = c - 1
                if 0 <= left < len(data[0]):
                    data[r][left] = "|"
                # Propogate right
                right = c + 1
                if 0 <= right < len(data[0]):
                    data[r][right] = "|"
        elif data[r][c] == ".":
            if data[r-1][c] == "|":
                data[r][c] = "|"

for line in data:        
    print(line)
print("Total times the beam split:", splitCount)