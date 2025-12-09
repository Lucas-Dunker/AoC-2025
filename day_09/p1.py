import heapq

with open("input.txt") as f:
    data = f.read().strip().splitlines()

coords = [tuple(coord.split(",")) for coord in data]

coords = set(coords)
areaHeapSet = set()

# Find areas between all points, convert them into a maxHeap, pop max area between two red tiles
def point_areas(points):
    def area(point1, point2):
        x1, y1 = map(float, point1)
        x2, y2 = map(float, point2)
        return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1), point1, point2
    
    areaHeap = []
    for x1, y1 in points:
        for x2, y2 in points:
            if (x1, y1) != (x2, y2):
                pointArea, p1, p2 = area((x1, y1), (x2, y2))
                
                if ((pointArea, p1, p2) not in areaHeapSet and (pointArea, p2, p1) not in areaHeapSet):
                    areaHeapSet.add((-pointArea, p1, p2))
                    areaHeap.append((-pointArea, p1, p2))
    heapq.heapify(areaHeap)
    return areaHeap

areaHeap = point_areas(coords)

maxArea = heapq.heappop(areaHeap)
print(f"Max Area: {-maxArea[0]} between points {maxArea[1]} and {maxArea[2]}")