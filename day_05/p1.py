with open("input.txt") as f:
    data = f.read().strip().split('\n\n')
    
ranges = data[0].splitlines()
ingredients = [int(ingredient) for ingredient in data[1].splitlines()]

numFresh = 0

for ingredient in ingredients:
    for curRange in ranges:
        beginning, end  = curRange.split("-")
        if int(beginning) <= ingredient <= int(end):
            numFresh += 1
            break
            
    
print(f'There are {numFresh} fresh ingredients.')    

