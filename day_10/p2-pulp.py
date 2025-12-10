from pulp import LpMinimize, LpProblem, LpVariable, lpSum, PULP_CBC_CMD

with open("input.txt") as f:
    lines = f.read().strip().splitlines()
    
data = [line.split(" ") for line in lines]
buttons = [[list(map(int, button[1:-1].split(","))) for button in line[1:-1]] for line in data]
joltages = [list(map(int, line[-1][1:-1].split(","))) for line in data]

def fewestPresses(targetJoltage, buttonList):
    prob = LpProblem("Joltage", LpMinimize)
    presses = [LpVariable(f"b{i}", lowBound=0, cat="Integer") for i in range(len(buttonList))]
    
    prob += lpSum(presses)
    
    for j in range(len(targetJoltage)):
        prob += lpSum(presses[i] for i in range(len(buttonList)) if j in buttonList[i]) == targetJoltage[j]
    
    prob.solve(PULP_CBC_CMD(msg=False))
    return int(sum((v.varValue or 0) for v in presses)) if prob.status == 1 else float('inf')

totalFewest = sum(fewestPresses(j, b) for b, j in zip(buttons, joltages))
print("Fewest button presses to configure all joltages:", totalFewest)