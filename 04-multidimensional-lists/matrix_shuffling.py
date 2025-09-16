def check_valid_indices(r1, c1, r2, c2, mat):
	return (0 <= r1 < len(mat) and 0 <= c1 < len(mat[0]) and
			0 <= r2 < len(mat) and 0 <= c2 < len(mat[0]))

rows, cols = [int(el) for el in input().split()]

matrix = []
for _ in range(rows):
	row_data = [el for el in input().split()]
	matrix.append(row_data)

cmd = input()
while cmd != 'END':
	tokens = cmd.split()
	if tokens[0] == 'swap' and len(tokens) == 5:
		row1, col1, row2, col2 = [int(x) for x in tokens[1:]]
		if check_valid_indices(row1, col1, row2, col2, matrix):
			matrix[row1][col1], matrix[row2][col2] = (matrix[row2][col2],
													  matrix[row1][col1])

			for i in range(len(matrix)):
				print(*matrix[i])

		else:
			print('Invalid input!')

	else:
		print('Invalid input!')

	cmd = input()
