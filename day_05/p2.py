with open("input.txt") as f:
    data = f.read().strip().split('\n\n')
    
ranges = data[0].splitlines()
numFresh = 0
allIntervals = []

# merge interval ranges
ranges = [x.split("-") for x in ranges]
ranges = [(int(x[0]), int(x[1])) for x in ranges]
ranges.sort(key = lambda x : [x[0], x[1]])

merged = [ranges[0]]

for start, end in ranges:
    lastEnd = merged[-1][1]
    if start <= lastEnd:
        merged[-1] = (merged[-1][0], max(lastEnd, end))
    else:
        merged.append((start, end))

# duplicates removed, now just sum ranges
for start, end in merged:
    numFresh += (end - start) + 1
            
    
print(f'There are {numFresh} ingredients considered fresh.')    

