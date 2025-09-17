rows = int(input())
matrix = []
for _ in range(rows):
	row_data = [int(x) for x in input().split()]
	matrix.append(row_data)

cmd = input()
while cmd != 'END':
	tokens = cmd.split()
	action = tokens[0]
	row, col, num = [int(x) for x in tokens[1:]]

	if not (0 <= row < rows and 0 <= col < rows):
		print('Invalid coordinates')
		cmd = input()
		continue

	if action == 'Add':
		matrix[row][col] += num
	elif action == 'Subtract':
		matrix[row][col] -= num

	cmd = input()

for mat_row in matrix:
	print(*mat_row)
