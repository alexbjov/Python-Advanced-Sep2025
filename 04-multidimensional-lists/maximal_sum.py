from sys import maxsize

rows, cols = [int(x) for x in input().split(' ')]

matrix = []
for _ in range(rows):
	row_data = [int(el) for el in input().split(' ')]
	matrix.append(row_data)

max_sum = -maxsize
max_row = -1
max_col = -1

for i in range(rows - 2):
	for j in range(cols - 2):
		current_sum = 0
		curr_elem = matrix[i][j]
		for row in range(i, i + 3):
			row_data = matrix[row][j:j+3]
			current_sum += sum(row_data)

		if max_sum < current_sum:
			max_sum = current_sum
			max_row = i
			max_col = j

print(f"Sum = {max_sum}")
for i in range(max_row, max_row + 3):
	print(*matrix[i][max_col:max_col+3])
