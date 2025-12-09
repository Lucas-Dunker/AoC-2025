with open("input.txt") as f:
    ranges = f.readlines()[0].split(",")
    
print("ID Ranges:", ranges)

# check if a given ID is invalid; an ID is invalid if it's made only of some sequence of repeated digits
def check_invalid(id):
    # min length of repeated digits: 1
    # max length of repeated digits: half the length of id, eg: 521521 = length of 3
    
    rangeMin, rangeMax = 1, len(id) // 2
    
    for r in range(rangeMin, rangeMax+1):
        # if a range doesn't split this ID evenly, then it can't be invalid
        if len(id) % r != 0:
            continue

        startIndices = [index * r for index in range(len(id) // r)]
        valueRanges = [id[index:index + r] for index in startIndices]
        
        if all(idRange == valueRanges[0] for idRange in valueRanges): # invalid ID if all subranges equal each other
            return True
        
    return False # No sequences of digits marked the ID as invalid

        
invalid_ids = []

for r in ranges:
    start, end = r.split("-")
    
    for id in range(int(start), int(end)+1):
        if check_invalid(str(id)):
            invalid_ids.append(id)

print("Invalid ID's:", invalid_ids)
print("Sum of all invalid ID's:", sum(invalid_ids))