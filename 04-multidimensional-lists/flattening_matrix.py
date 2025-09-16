rows = int(input())

flattened_matrix = []
for _ in range(rows):
	row_data = [int(elem) for elem in input().split(', ')]
	for el in row_data:
		flattened_matrix.append(el)

print(flattened_matrix)
