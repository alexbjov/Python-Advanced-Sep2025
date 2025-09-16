from sys import maxsize

rows, cols = [int(x) for x in input().split(', ')]

matrix = []
for _ in range(rows):
	row_data = [int(el) for el in input().split(', ')]
	matrix.append(row_data)

# print(matrix)
max_sum = -maxsize
sub_matrix = None

for i in range(rows - 1):
	for j in range(cols - 1):
		top_left = matrix[i][j]
		top_right = matrix[i][j+1]
		bottom_left = matrix[i+1][j]
		bottom_right = matrix[i+1][j+1]
		sum_members = top_left + top_right + bottom_left + bottom_right

		if max_sum < sum_members:
			max_sum = sum_members
			sub_matrix = [[top_left, top_right], [bottom_left, bottom_right]]

for row in sub_matrix:
	print(*row)

print(max_sum)
