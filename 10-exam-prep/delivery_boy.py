rows, cols = map(int, input().split())

matrix = []
boy = [-1, -1]
start_pos = None

for row in range(rows):
	row_data = list(input())
	matrix.append(row_data)
	for col in range(cols):
		if matrix[row][col] == 'B':
			boy = [row, col]
			start_pos = (row, col)

boy_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
took_pizza = False

while True:
	cmd = input()
	move = boy_moves[cmd]
	
	new_row = boy[0] + move[0]
	new_col = boy[1] + move[1]
	
	if not (0 <= new_row < rows and 0 <= new_col < cols):
		print("The delivery is late. Order is canceled.")
		matrix[start_pos[0]][start_pos[1]] = ' '
		break
	
	elif matrix[new_row][new_col] == '*':
		continue
	
	elif matrix[new_row][new_col] == 'P':
		print("Pizza is collected. 10 minutes for delivery.")
		took_pizza = True
		matrix[new_row][new_col] = 'R'
	
	elif matrix[new_row][new_col] == 'A':
		if took_pizza:
			print("Pizza is delivered on time! Next order...")
			matrix[new_row][new_col] = 'P'
			break
	
	elif matrix[new_row][new_col] == '-':
		matrix[new_row][new_col] = '.'
	
	boy = [new_row, new_col]

for mat_row in matrix:
	print("".join(mat_row))
