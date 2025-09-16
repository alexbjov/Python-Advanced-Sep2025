rows, cols = map(int, input().split(', '))

matrix_sums = [0] * cols
for _ in range(rows):
	row_data = [int(el) for el in input().split()]
	for i in range(len(matrix_sums)):
		matrix_sums[i] += row_data[i]

print(*matrix_sums, sep='\n')
