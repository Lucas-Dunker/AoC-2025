with open("input.txt") as f:
    lines = f.read().strip().splitlines()
    
data = [line.split(" ") for line in lines]
indicators = [list(line[0][1:-1]) for line in data]
buttons = [[list(map(int, button[1:-1].split(","))) for button in line[1:-1]] for line in data]
joltages = [list(map(int, line[-1][1:-1].split(","))) for line in data]

# calculate the fewest button presses to match joltage levels with the diagram
def fewestPresses(targetJoltage, buttonList):
    fewestPresses = float('inf')
    
    def backtrack(buttonIdx, numPresses, curJoltage):
        nonlocal fewestPresses
        if curJoltage == targetJoltage:
            fewestPresses = min(fewestPresses, numPresses)
            return
        if numPresses >= fewestPresses: 
            return # prune if current path is worse than best solution
        if any(curJoltage[j] > targetJoltage[j] for j in range(len(targetJoltage))):
            return # prune if current path isn't feasible
        if buttonIdx >= len(buttonList):
            return # prune if we're out of buttons to select
        
        # Calculate maximum amount of times we can press the current button
        button = buttonList[buttonIdx]
        if button:
            maxPresses = min(targetJoltage[j] - curJoltage[j] for j in button)
        else:
            maxPresses = 0
        
        # Iterate through all possible joltage combinations (within reason)
        for presses in range(maxPresses + 1):
                newJoltage = curJoltage[:]
                for j in button:
                    newJoltage[j] += presses
                backtrack(buttonIdx + 1, numPresses + presses, newJoltage)

    curJoltage = [0] * len(targetJoltage)
    backtrack(0, 0, curJoltage)
    return fewestPresses

totalFewest = 0
for indicator, buttonList, joltageList in zip(indicators, buttons, joltages):
    curPresses = fewestPresses(joltageList, buttonList)
    print(curPresses)
    totalFewest += curPresses
    
print("Fewest button presses to configure all joltages:", totalFewest)

# Backtracking template:
# # def backtrack(candidate):
# if find_solution(candidate):
#     output(candidate)
#     return

# # iterate all possible candidates.
# for next_candidate in list_of_candidates:
#     if is_valid(next_candidate):
#         # try this partial candidate solution
#         place(next_candidate)
#         # given the candidate, explore further.
#         backtrack(next_candidate)
#         # backtrack
#         remove(next_candidate)