with open("input.txt") as f:
    batteries = [line.strip() for line in f.readlines()]
    
total = 0
joltageLength = 12

for bank in batteries:
    bankIndices = []
    
    # keep finding largest number that satisfies our conditions
    while len(bankIndices) < joltageLength:
        # take the largest number that still lets us get to joltageLength amount of indices
        leftBound = bankIndices[-1]+1 if len(bankIndices) > 0 else 0
        rightBound = len(bank) - joltageLength + len(bankIndices) + 1
        
        bankIndices.append(bank.index(max(bank[leftBound : rightBound]), leftBound, rightBound))
        print(leftBound, rightBound, bankIndices)
    
    maxLine = ""
    print(bankIndices)
    for idx in bankIndices:
        maxLine += bank[idx]
    print(maxLine)
    total += int(maxLine)


print("Total Output Joltage: ", total)