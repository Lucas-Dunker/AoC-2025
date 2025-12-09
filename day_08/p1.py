import heapq

with open("input.txt") as f:
    data = f.read().strip().splitlines()

coords = [tuple(coord.split(",")) for coord in data]

coords = set(coords)
distanceHeapSet = set()

# Find distances between all points, convert them into a minheap
def point_distances(points):
    def distance_3d(point1, point2):
        x1, y1, z1 = map(float, point1)
        x2, y2, z2 = map(float, point2)
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5, point1, point2
    
    distanceHeap = []
    for x1, y1, z1 in points:
        for x2, y2, z2 in points:
            if (x1, y1, z1) != (x2, y2, z2):
                dist, p1, p2 = distance_3d((x1, y1, z1), (x2, y2, z2))
                
                if ((dist, p1, p2) not in distanceHeapSet and (dist, p2, p1) not in distanceHeapSet):
                    distanceHeapSet.add((dist, p1, p2))
                    distanceHeap.append((dist, p1, p2))
    heapq.heapify(distanceHeap)
    return distanceHeap

distanceHeap = point_distances(coords)

# Connect boxes with other boxes/circuits that have the smallest distance
connections = 1000
circuits = []

for coord in coords:
    circuits.append([coord])

for i in range(connections):
        def box_in_circuit(p):
            for i, circuit in enumerate(circuits):
                if p in circuit:
                    return i
            return -1
        
        dist, p1, p2 = heapq.heappop(distanceHeap)
        p1Idx, p2Idx = box_in_circuit(p1), box_in_circuit(p2)
        if p1Idx == -1 and p2Idx == -1:
            circuits.append([p1, p2]) 
        elif p1Idx == -1 and p2Idx != -1:
            circuits[p2Idx].append(p1)
        elif p1Idx != -1 and p2Idx == -1:
            circuits[p1Idx].append(p2)
        else:
            if p1Idx != p2Idx:
                circuits[p1Idx].extend(circuits[p2Idx])
                del circuits[p2Idx]

# Multiply together the sizes of the 3 largest circuits
circuitSizes = sorted([len(circuit) for circuit in circuits], reverse=True)
product = circuitSizes[0] * circuitSizes[1] * circuitSizes[2]

print(circuitSizes)
print("Product of the sizes of the 3 largest circuits:", product)