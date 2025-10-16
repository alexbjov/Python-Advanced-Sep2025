rows, cols = map(int, input().split(','))

matrix = []
mouse = [-1, -1]
total_cheese = 0
for row in range(rows):
	row_data = list(input())
	matrix.append(row_data)
	for col in range(cols):
		if matrix[row][col] == 'M':
			mouse = [row, col]
		elif matrix[row][col] == 'C':
			total_cheese += 1

mouse_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

cheese_now = 0
command = input()
while command != 'danger':
	move = mouse_moves[command]
	new_row = mouse[0] + move[0]
	new_col = mouse[1] + move[1]
	
	if not (0 <= new_row < rows and 0 <= new_col < cols):
		print("No more cheese for tonight!")
		break
	
	if matrix[new_row][new_col] == '@':
		command = input()
		continue
	
	matrix[mouse[0]][mouse[1]] = '*'
	if matrix[new_row][new_col] == 'C':
		cheese_now += 1
		if cheese_now == total_cheese:
			matrix[new_row][new_col] = 'M'
			mouse = [new_row, new_col]
			print("Happy mouse! All the cheese is eaten, good night!")
			break
	
	elif matrix[new_row][new_col] == 'T':
		matrix[new_row][new_col] = 'M'
		mouse = [new_row, new_col]
		print("Mouse is trapped!")
		break
	
	matrix[new_row][new_col] = 'M'
	mouse = [new_row, new_col]
	command = input()

else:
	print("Mouse will come back later!")

for mat_row in matrix:
	print("".join(mat_row))
