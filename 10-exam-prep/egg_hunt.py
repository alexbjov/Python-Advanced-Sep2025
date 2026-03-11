n_size = int(input())
current_eggs = 5
target_eggs = 10
matrix = []
bunny_x, bunny_y = -1, -1

for i in range(n_size):
    row_data = list(input())
    matrix.append(row_data)

    if "B" in row_data:
        j = row_data.index("B")
        bunny_x, bunny_y = i, j

bunny_moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

start_x, start_y = bunny_x, bunny_y

cmd = input()
while cmd != "stop":
    new_move = bunny_moves[cmd]
    new_bunny_x = start_x + new_move[0]
    new_bunny_y = start_y + new_move[1]

    matrix[start_x][start_y] = '.'
    if new_bunny_x < 0 or new_bunny_x >= n_size:
        start_x, start_y = bunny_x, bunny_y
        matrix[start_x][start_y] = 'B'
        cmd = input()
        continue

    elif new_bunny_y < 0 or new_bunny_y >= n_size:
        start_x, start_y = bunny_x, bunny_y
        matrix[start_x][start_y] = 'B'
        cmd = input()
        continue

    if matrix[new_bunny_x][new_bunny_y] == 'E':
        current_eggs += 1

    elif matrix[new_bunny_x][new_bunny_y] == 'T':
        current_eggs -= 1

    elif matrix[new_bunny_x][new_bunny_y] == 'F':
        current_eggs *= 2

    matrix[new_bunny_x][new_bunny_y] = 'B'
    start_x, start_y = new_bunny_x, new_bunny_y

    if current_eggs == 0 or current_eggs >= target_eggs:
        break

    cmd = input()

if current_eggs >= target_eggs:
    print(f"Easter Bunny wins! Collected eggs: {current_eggs}.")
elif current_eggs == 0:
    print("Game over! Easter Bunny has no eggs left.")
elif cmd == "stop":
    print(f"Easter Bunny stopped hunting with {current_eggs} eggs.")

for mat_row in matrix:
    print(*mat_row, sep='')
