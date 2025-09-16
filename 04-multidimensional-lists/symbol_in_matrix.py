rows = int(input())

matrix = []
for _ in range(rows):
	row_data = [elem for elem in input()]
	matrix.append(row_data)

searched_symbol = input()
is_found = False
for i in range(rows):
	for j in range(rows):
		if searched_symbol == matrix[i][j]:
			print(f'({i}, {j})')
			is_found = True
			break

	if is_found:
		break

else:
	print(f'{searched_symbol} does not occur in the matrix')
