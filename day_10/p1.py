with open("input.txt") as f:
    lines = f.read().strip().splitlines()
    
data = [line.split(" ") for line in lines]
indicators = [list(line[0][1:-1]) for line in data]
buttons = [[list(map(int, button[1:-1].split(","))) for button in line[1:-1]] for line in data]
joltages = [list(map(int, line[-1][1:-1].split(","))) for line in data]

# calculate the fewest button presses to match an empty indicator's lights with the diagram
def fewestPresses(targetIndicator, buttonList):
    def pressButton(indicator, buttonGroup):
        for button in buttonGroup:
            if indicator[button] == "#":
                indicator[button] = '.'
            elif indicator[button] == '.':
                indicator[button] = '#'
        return indicator

    fewestPresses = float('inf')
    
    def backtrack(startIdx, numPresses, curIndicator):
        nonlocal fewestPresses
        if numPresses >= fewestPresses: # prune if already worse than best solution
            return
        if curIndicator == targetIndicator:
            fewestPresses = min(fewestPresses, numPresses)
            return
        
        for i in range(startIdx, len(buttonList)):
            newIndicator = pressButton(curIndicator[:], buttonList[i])
            backtrack(i + 1, numPresses + 1, newIndicator)

    curIndicator = ["."] * len(targetIndicator)
    backtrack(0, 0, curIndicator)
    return fewestPresses

totalFewest = 0
for indicator, buttonList, joltageList in zip(indicators, buttons, joltages):
    totalFewest += fewestPresses(indicator, buttonList)
    
print("Fewest button presses to configure all indicators:", totalFewest)

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