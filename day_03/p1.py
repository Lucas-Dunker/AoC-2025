with open("input.txt") as f:
    batteries = [line.strip() for line in f.readlines()]
    
total = 0

for bank in batteries:
    maxIdx_1 = 0
    
    # find largest number
    for idx in range(len(bank)-1):
        if int(bank[idx]) > int(bank[maxIdx_1]):
            maxIdx_1 = idx
            
    maxIdx_2 = maxIdx_1 + 1
    # find largest number that's after maxIdx_1
    for idx in range(maxIdx_1+1, len(bank)):
        if int(bank[idx]) > int(bank[maxIdx_2]):
            maxIdx_2 = idx
    
    maxLine = int(bank[maxIdx_1] + bank[maxIdx_2])
    print(maxLine)
    total += maxLine


print("Total Output Joltage: ", total)