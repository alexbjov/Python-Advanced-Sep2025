rows = int(input())
matrix = [[int(el) for el in input().split(' ')] for _ in range(rows)]

primary_diagonal = []
secondary_diagonal = []

for i in range(rows):
	for j in range(rows):
		if i == j:
			primary_diagonal.append(matrix[i][j])
		if i + j == len(matrix[i]) - 1:
			secondary_diagonal.append(matrix[i][j])

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
