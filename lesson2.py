map1 = [
    [12, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 24]
]

map2 = [
    [12, 1, 0, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 24]
]
map=map1

current_position_x = 0
current_position_y = 0

# le step 1
print(f"le position x - {current_position_x}")
print(f"le position y - {current_position_y}")
can_move_right = map[current_position_y][current_position_x+1] == 0
can_move_left = map[current_position_y+1][current_position_x] == 0

if can_move_right:
    print("should move le right")
    current_position_x = current_position_x+1
if can_move_left:
    print("le should move le down")
    current_position_y = current_position_y+1

# le step 2
print(f"le position x - {current_position_x}")
print(f"le position y - {current_position_y}")
can_move_right = map[current_position_y][current_position_x+1] == 0
can_move_left = map[current_position_y+1][current_position_x] == 0

if can_move_right:
    print("should move le right")
    current_position_x = current_position_x+1
if can_move_left:
    print("le should move le down")
    current_position_y = current_position_y+1

# le step 3
print(f"le position x - {current_position_x}")
print(f"le position y - {current_position_y}")
can_move_right = map[current_position_y][current_position_x+1] == 0
can_move_left = map[current_position_y+1][current_position_x] == 0

if can_move_right:
    print("should move le right")
    current_position_x = current_position_x+1
if can_move_left:
    print("le should move le down")
    current_position_y = current_position_y+1

# le step 4
print(f"le position x - {current_position_x}")
print(f"le position y - {current_position_y}")
can_move_right = map[current_position_y][current_position_x+1] == 0
can_move_left = map[current_position_y+1][current_position_x] == 0

if can_move_right:
    print("should move le right")
    current_position_x = current_position_x+1
if can_move_left:
    print("le should move le down")
    current_position_y = current_position_y+1

# le step 5
print(f"le position x - {current_position_x}")
print(f"le position y - {current_position_y}")
can_move_right = map[current_position_y][current_position_x+1] == 0
can_move_left = map[current_position_y+1][current_position_x] == 0

if can_move_right:
    print("should move le right")
    current_position_x = current_position_x+1
if can_move_left:
    print("le should move le down")
    current_position_y = current_position_y+1


'''
print("can you move right")
print(map[0][1] == 0)
print("can you move to botom")
print(map[0][0] == 0)

print("can you move right")
print(map[0][2] == 0)
print("can you move left")
print(map[1][1] == 0)

print("can you move right")
print(map[1][2] == 0)
print("can you move left")
print(map[2][1] == 0)
'''