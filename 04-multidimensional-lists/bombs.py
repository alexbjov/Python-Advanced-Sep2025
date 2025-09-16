rows = int(input())

matrix = []
for _ in range(rows):
	row_data = [int(x) for x in input().split()]
	matrix.append(row_data)
	# print(row_data)

cmds = input().split()
coordinates = []
for cmd in cmds:
	b_x, b_y = map(int, cmd.split(','))
	coordinates.append((b_x, b_y))
# print(coordinates)

for bomb_x, bomb_y in coordinates:
	# print(bomb_x, bomb_y)
	start_x = max(bomb_x - 1, 0)
	end_x = min(bomb_x + 2, rows)
	start_y = max(bomb_y - 1, 0)
	end_y = min(bomb_y + 2, rows)
	bomb_power = matrix[bomb_x][bomb_y]
	for i in range(start_x, end_x):
		for j in range(start_y, end_y):
			if matrix[i][j] > 0:
				matrix[i][j] -= bomb_power

counter_alive_cells = 0
sum_alive_cells = 0
for i in range(rows):
	for j in range(rows):
		if matrix[i][j] > 0:
			counter_alive_cells += 1
			sum_alive_cells += matrix[i][j]

print(f'Alive cells: {counter_alive_cells}')
print(f'Sum: {sum_alive_cells}')

for mat_row in matrix:
	print(*mat_row)
