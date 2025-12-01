n = int(input())
directions = input().split(", ")

squirrel_pos = [-1, -1]
matrix = []
for i in range(n):
    row_data = list(input())
    matrix.append(row_data)
    if 's' in row_data:
        j = row_data.index('s')
        squirrel_pos = [i, j]

moves_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

hazelnuts = 0

for direction in directions:
    move_x, move_y = moves_mapper[direction]
    
    new_squirrel_x = squirrel_pos[0] + move_x
    new_squirrel_y = squirrel_pos[1] + move_y
    
    matrix[squirrel_pos[0]][squirrel_pos[1]] = "*"
    if not 0 <= new_squirrel_x < n or not 0 <= new_squirrel_y < n:
        print("The squirrel is out of the field.")
        break
    
    if matrix[new_squirrel_x][new_squirrel_y] == "t":
        print(f"Unfortunately, the squirrel stepped on a trap...")
        break
    
    if matrix[new_squirrel_x][new_squirrel_y] == "h":
        hazelnuts += 1
        if hazelnuts == 3:
            matrix[new_squirrel_x][new_squirrel_y] = "*"
            print("Good job! You have collected all hazelnuts!")
            break
    
    matrix[new_squirrel_x][new_squirrel_y] = 's'
    squirrel_pos = [new_squirrel_x, new_squirrel_y]

else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")
