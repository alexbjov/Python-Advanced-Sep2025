from collections import deque

rows, cols = [int(x) for x in input().split()]
text = deque(input())

matrix = []

for row in range(rows):
	matrix.append([""] * cols)
	for col in range(cols):
		if row % 2 == 0:
			matrix[row][col] = text[0]
			# print("Even: ", matrix)
		else:
			matrix[row][- 1 - col] = text[0]
			# print("Odd: ", matrix)
		text.rotate(-1)
		# print("Rotated: ", matrix)

[print(*row, sep="") for row in matrix]
