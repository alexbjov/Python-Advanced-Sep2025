rows, cols = [int(x) for x in input().split(', ')]

matrix = []
total_sum = 0
for _ in range(rows):
	row_data = [int(x) for x in input().split(', ')]
	total_sum += sum(row_data)
	matrix.append(row_data)

print(total_sum)
print(matrix)
