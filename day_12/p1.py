with open("input.txt") as f:
    lines = f.read().strip().split("\n\n")
    
data = [line.split("\n") for line in lines]

def parseData(data):
    shapes = {} # dict of shape index to shape grid
    for shape in data[0:-1]:
        shapes[int(shape[0][0:-1])] = shape[1:]
        
    regions = [] # 2d array of width x length tuples and shape quantities
    for regionLine in data[-1]:
        numbers = regionLine.split(" ")
        region = tuple(map(int, numbers[0][0:-1].split("x")))
        quantities = list(map(int, numbers[1:]))
        regions.append([region, quantities])
        
    return shapes, regions

shapes, regions = parseData(data)
print(shapes)
print(regions)

# Can this region fit all of its presents? Rotations and flips are allowed.
# After investigating how difficult this problem is, it seems like there's a trick.... (not my own idea)
def canFit(region):
    dims = region[0]
    regionArea = dims[0] * dims[1]
    
    shapeQuantities = region[1]
    shapeSum = 0
    print(shapeQuantities)
    for idx in range(len(shapeQuantities)):
        shapeSum += 7 * shapeQuantities[idx]
    print(shapeSum)
    
    return shapeSum <= regionArea

fittingSections = 0

for region in regions:
    if canFit(region):
        fittingSections += 1
        
print("Regions that can fit their presents:", fittingSections)