n_rows = int(input())
matrix = []
ship_x, ship_y = -1, -1
max_hits = 3
start_hits = 0
num_cruisers = 3

for i in range(n_rows):
    data_row = list(input())
    if "S" in data_row:
        j = data_row.index("S")
        ship_x, ship_y = i, j
    matrix.append(data_row)

ship_moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while start_hits < max_hits and num_cruisers > 0:
    cmd = input()
    new_ship_x = ship_x + ship_moves[cmd][0]
    new_ship_y = ship_y + ship_moves[cmd][1]

    if matrix[new_ship_x][new_ship_y] == "*":
        start_hits += 1

    elif matrix[new_ship_x][new_ship_y] == "C":
        num_cruisers -= 1

    matrix[ship_x][ship_y] = "-"
    matrix[new_ship_x][new_ship_y] = "S"
    ship_x, ship_y = new_ship_x, new_ship_y

if start_hits == max_hits:
    print(f"Mission failed, U-9 disappeared! Last known coordinates [{ship_x}, {ship_y}]!")
elif num_cruisers == 0:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")

for mat_row in matrix:
    print(*mat_row, sep="")
