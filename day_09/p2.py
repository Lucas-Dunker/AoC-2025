import heapq
from itertools import combinations

# Too much code + variables this time, so breaking into functions and 
# moving driver logic to bottom

def parse_input(filename):
    with open(filename) as f:
        data = f.read().strip().splitlines()
    coords = [tuple(map(int, coord.split(","))) for coord in data]
    return coords, set(coords)


def build_boundary(coords):
    boundary = set()
    for i in range(len(coords)):
        x1, y1 = coords[i]
        x2, y2 = coords[(i + 1) % len(coords)]
        
        if x1 == x2:  # Vertical line
            for y in range(min(y1, y2), max(y1, y2) + 1):
                boundary.add((x1, y))
        else:  # Horizontal line
            for x in range(min(x1, x2), max(x1, x2) + 1):
                boundary.add((x, y1))
    
    return boundary


def get_bounds(boundary):
    min_x = min(p[0] for p in boundary)
    max_x = max(p[0] for p in boundary)
    min_y = min(p[1] for p in boundary)
    max_y = max(p[1] for p in boundary)
    return min_x, max_x, min_y, max_y


def compute_row_ranges(boundary, min_x, max_x, min_y, max_y):
    yRanges = {}
    for y in range(min_y, max_y + 1):
        inside = False
        row_min_x = None
        row_max_x = None
        
        for x in range(min_x, max_x + 1):
            is_green = False
            if (x, y) in boundary:
                above = (x, y - 1) in boundary
                below = (x, y + 1) in boundary
                if above and below:
                    inside = not inside
                is_green = True
            elif inside:
                is_green = True
            
            if is_green:
                if row_min_x is None:
                    row_min_x = x
                row_max_x = x
        
        if row_min_x is not None:
            yRanges[y] = (row_min_x, row_max_x)
    
    return yRanges


def compute_col_ranges(boundary, min_x, max_x, min_y, max_y):
    xRanges = {}
    for x in range(min_x, max_x + 1):
        inside = False
        col_min_y = None
        col_max_y = None
        
        for y in range(min_y, max_y + 1):
            is_green = False
            if (x, y) in boundary:
                left = (x - 1, y) in boundary
                right = (x + 1, y) in boundary
                if left and right:
                    inside = not inside
                is_green = True
            elif inside:
                is_green = True
            
            if is_green:
                if col_min_y is None:
                    col_min_y = y
                col_max_y = y
        
        if col_min_y is not None:
            xRanges[x] = (col_min_y, col_max_y)
    
    return xRanges


def build_area_heap(coords_set):
    areaHeap = []
    for p1, p2 in combinations(coords_set, 2):
        x1, y1 = p1
        x2, y2 = p2
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        areaHeap.append((-area, p1, p2))
    heapq.heapify(areaHeap)
    return areaHeap


def check_bounds(p1, p2, xRanges, yRanges):
    x1, y1 = p1
    x2, y2 = p2
    
    minX, maxX = min(x1, x2), max(x1, x2)
    minY, maxY = min(y1, y2), max(y1, y2)
    
    all_rows_valid = all(
        y in yRanges and yRanges[y][0] <= minX and maxX <= yRanges[y][1]
        for y in range(minY, maxY + 1)
    )
    
    all_cols_valid = all(
        x in xRanges and xRanges[x][0] <= minY and maxY <= xRanges[x][1]
        for x in range(minX, maxX + 1)
    )
    
    return all_rows_valid and all_cols_valid


def find_largest_rectangle(areaHeap, xRanges, yRanges):
    while areaHeap:
        maxArea, p1, p2 = heapq.heappop(areaHeap)
        
        if check_bounds(p1, p2, xRanges, yRanges):
            return -maxArea, p1, p2
    
    return None, None, None

coords, coords_set = parse_input("input.txt")

boundary = build_boundary(coords)
min_x, max_x, min_y, max_y = get_bounds(boundary)

yRanges = compute_row_ranges(boundary, min_x, max_x, min_y, max_y)
xRanges = compute_col_ranges(boundary, min_x, max_x, min_y, max_y)

areaHeap = build_area_heap(coords_set)
area, p1, p2 = find_largest_rectangle(areaHeap, xRanges, yRanges)

if area:
    print(f"Max Area within Bounds: {area} between points {p1} and {p2}")
else:
    print("No valid rectangle found")
    
# Took around 30 minutes of running time for the input, but got the right answer!