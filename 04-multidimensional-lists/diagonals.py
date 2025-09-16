rows = int(input())
matrix = [[int(el) for el in input().split(', ')] for _ in range(rows)]

primary_diagonal = []
secondary_diagonal = []

for i in range(rows):
	for j in range(rows):
		if i == j:
			primary_diagonal.append(matrix[i][j])
		if i + j == len(matrix[i]) - 1:
			secondary_diagonal.append(matrix[i][j])

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum:"
	  f" {sum(primary_diagonal)}")
print(f"Secondary diagonal:"
	  f" {', '.join([str(x) for x in secondary_diagonal])}. "
	  f"Sum: {sum(secondary_diagonal)}")
