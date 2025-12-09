from collections import defaultdict

with open("input.txt") as f:
    data = f.read().strip().splitlines()

numbers = data[:-1]
operators = data[-1].split()

# Group digits into columns
columns = defaultdict(list)
for row in numbers:
    for col_idx, digit in enumerate(row):
        columns[col_idx].append(digit)

# Convert columns to groups of numbers
groups = []
curGroup = []
for col_values in columns.values():
    curNum = ("".join(col_values))
    if curNum.strip() == "":
        groups.append(curGroup)
        curGroup = []
    else:
        curGroup.append(int(curNum))
groups.append(curGroup)

# Calculate total based on operators
total = 0
for group, op in zip(groups, operators):
    if op == "+":
        total += sum(group)
    elif op == "*":
        result = 1
        for val in group:
            result *= val
        total += result

print("The grand total is:", total)
