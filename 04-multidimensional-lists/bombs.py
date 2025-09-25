rows = int(input())

matrix = []
for _ in range(rows):
	row_data = [int(x) for x in input().split()]
	matrix.append(row_data)

cmds = input().split()
coordinates = []
for cmd in cmds:
	b_x, b_y = list(map(int, cmd.split(',')))
	coordinates.append((b_x, b_y))

possible_moves = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1),
				  (1, 1), (0, 0))

for bomb_x, bomb_y in coordinates:
	if matrix[bomb_x][bomb_y] <= 0:
		continue
	
	for move in possible_moves:
		next_row = bomb_x + move[0]
		next_col = bomb_y + move[1]
		if not 0 <= next_row < rows or not 0 <= next_col < rows:
			continue
		
		bomb_power = matrix[bomb_x][bomb_y]
		if matrix[next_row][next_col] > 0:
			matrix[next_row][next_col] -= bomb_power

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
