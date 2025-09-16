rows = int(input())

matrix = []
sum_primary_diagonal = 0

for i in range(rows):
	row_data = [int(elem) for elem in input().split()]
	matrix.append(row_data)
	sum_primary_diagonal += matrix[i][i]

print(sum_primary_diagonal)
