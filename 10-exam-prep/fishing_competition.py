rows = int(input())

matrix: list[list[str]] = []
ship = [-1, -1]
for row in range(rows):
	row_data = list(input())
	matrix.append(row_data)
	if 'S' in row_data:
		col = row_data.index('S')
		ship = [row, col]

ship_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1), }

target_fish = 20
caught_fish = 0
has_died = False

command = input()
while command != 'collect the nets':
	moves = ship_moves[command]
	
	new_row = ship[0] + moves[0]
	new_col = ship[1] + moves[1]
	matrix[ship[0]][ship[1]] = '-'
	if new_row == rows:
		new_row = 0
	elif new_row < 0:
		new_row = rows - 1
	elif new_col == rows:
		new_col = 0
	elif new_col < 0:
		new_col = rows - 1
	
	if matrix[new_row][new_col].isdigit():
		caught_fish += int(matrix[new_row][new_col])
		matrix[new_row][new_col] = 'S'
	
	elif matrix[new_row][new_col] == 'W':
		has_died = True
		caught_fish = 0
		ship = [new_row, new_col]
		break
	
	else:
		matrix[new_row][new_col] = 'S'
	
	ship = [new_row, new_col]
	command = input()

if has_died:
	print(
		f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{ship[0]},{ship[1]}]")

elif caught_fish >= target_fish:
	print(f"Success! You managed to reach the quota!")

else:
	print(
		f"You didn't catch enough fish and didn't reach the quota! You need {target_fish - caught_fish} tons of fish more.")

if caught_fish > 0:
	print(f"Amount of fish caught: {caught_fish} tons.")

if not has_died:
	for mat_row in matrix:
		print(*mat_row, sep="")
