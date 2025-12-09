from collections import defaultdict

with open("input.txt") as f:
    data = f.read().strip().splitlines()
    
data = [line.split() for line in data]
totalSum = 0

columnValues = defaultdict(list) # col Idx -> list of values

for r in range(len(data)):
    for c in range(len(data[0])):
        columnValues[c].append(data[r][c])

for column in columnValues.values():
    if column[-1] == "+":
        totalSum += sum(int(val) for val in column[0:len(column)-1])
    elif column[-1] == "*":
        start = 1
        for val in column[0:len(column)-1]:
            start *= int(val)
        totalSum += start
        
print("The grand total is:", totalSum)