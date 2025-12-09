file_path = 'input.txt'
rotations = []

with open(file_path, 'r') as file:
    for line in file:
        rotations.append(line.strip())
        
# The actual password is the number of times the dial is left pointing at 0 after any rotation in the sequence.
num_zeroed = 0
cur_num = 50

for rotation in rotations:
    direction = rotation[0]
    position = int(rotation[1:])
    if direction == "L":
        cur_num = (cur_num - position) % 100
    elif direction == "R":
        cur_num = (cur_num + position) % 100
        
    # Counting the times the dial points at 0 after a rotation
    if cur_num == 0:
        num_zeroed += 1

print(num_zeroed)