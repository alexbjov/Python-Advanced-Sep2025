n_rows = int(input())
num_of_car = input()

has_won_race = False

kms_passed = 0
kms_per_move = 10
kms_per_tunnel_move = 30
car_x, car_y = 0, 0
tunnel = {}

matrix = []
for i in range(n_rows):
    row_data = input().split()
    if "T" in row_data:
        j = row_data.index("T")
        if "t1" not in tunnel:
            tunnel["t1"] = (i, j)
        elif "t2" not in tunnel:
            tunnel["t2"] = (i, j)

    matrix.append(row_data)
matrix[car_x][car_y] = "C"

car_moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

cmd = input()
while cmd != "End":
    new_move = car_moves[cmd]
    new_car_x = car_x + new_move[0]
    new_car_y = car_y + new_move[1]

    matrix[car_x][car_y] = "."
    if matrix[new_car_x][new_car_y] == ".":
        kms_passed += kms_per_move

    elif matrix[new_car_x][new_car_y] == "T":
        matrix[new_car_x][new_car_y] = "."
        kms_passed += kms_per_tunnel_move
        if tunnel["t1"] == (new_car_x, new_car_y):
            new_car_x, new_car_y = tunnel["t2"]
        else:
            new_car_x, new_car_y = tunnel["t1"]

    elif matrix[new_car_x][new_car_y] == "F":
        kms_passed += kms_per_move

        matrix[new_car_x][new_car_y] = "C"
        car_x, car_y = new_car_x, new_car_y
        has_won_race = True
        break

    matrix[new_car_x][new_car_y] = "C"
    car_x, car_y = new_car_x, new_car_y

    cmd = input()

if cmd == "End" and not has_won_race:
    print(f"Racing car {num_of_car} DNF.")
elif has_won_race:
    print(f"Racing car {num_of_car} finished the stage!")

print(f"Distance covered {kms_passed} km.")

for mat_row in matrix:
    print(*mat_row, sep="")
