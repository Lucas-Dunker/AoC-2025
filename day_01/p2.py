with open("input.txt") as f:
    rotations = [line.strip() for line in f]

zero_passes = 0
cur_num = 50

for rotation in rotations:
    direction = rotation[0]
    distance = int(rotation[1:])
    
    if direction == "L":
        # Count zeros during left rotation
        zero_passes += (distance + (100 if cur_num > 0 else 0) - cur_num) // 100
        cur_num = (cur_num - distance) % 100
    elif direction == "R":
        # Count zeros during right rotation
        zero_passes += (cur_num + distance) // 100
        cur_num = (cur_num + distance) % 100

print(zero_passes)