elements = input().split('|')

matrix = []
for i in range(len(elements) - 1, -1, -1):
	row_data = elements[i].split()
	if row_data:
		matrix.append(row_data)

for row in matrix:
	print(*row, end=' ')
