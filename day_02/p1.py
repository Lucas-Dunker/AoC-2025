with open("input.txt") as f:
    ranges = f.readlines()[0].split(",")
    
print(ranges)

# Goal: sum all invalid ID's given a list of ID ranges
sum = 0

# check if a given ID is invalid; an ID is invalid if it's made only of some sequence of digits repeated twice
def check_invalid(id):
    # for an ID to consist of 2 digits repeated twice, it must be of even length
    if len(id) % 2 != 0:
        return False

    i, j = 0, len(id) // 2 # should always be a whole number
    while j < len(id):
        if id[i] != id[j]:
            return False
        elif id[i] == id[j]:
            i += 1
            j += 1
    
    return True

# iterate over ID ranges
for r in ranges:
    start, end = r.split("-")
    
    for id in range(int(start), int(end)+1):
        if check_invalid(str(id)):
            sum += id

print("Sum of all invalid ID's:", sum)