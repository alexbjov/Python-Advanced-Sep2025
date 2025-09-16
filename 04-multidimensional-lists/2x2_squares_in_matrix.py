rows, cols = [int(x) for x in input().split(' ')]

matrix = []
for _ in range(rows):
	row_data = [el for el in input().split(' ')]
	matrix.append(row_data)

counter = 0

for i in range(rows - 1):
	for j in range(cols - 1):
		top_left = matrix[i][j]
		top_right = matrix[i][j+1]
		bottom_left = matrix[i+1][j]
		bottom_right = matrix[i+1][j+1]
		if (top_left == top_right and top_left == bottom_left and top_left ==
				bottom_right):
			counter += 1

print(counter)
