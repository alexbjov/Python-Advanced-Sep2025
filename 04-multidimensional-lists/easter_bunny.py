from sys import maxsize

rows = int(input())

matrix = []
b_row, b_col = -1, -1
bunny_moves = {
	"up": (-1, 0),
	"down": (1, 0),
	"left": (0, -1),
	"right": (0, 1)
}

for row in range(rows):
	matrix.append(input().split())
	for col in range(rows):
		if matrix[row][col] == 'B':
			b_row = row
			b_col = col

# for mat_row in matrix:
# 	print(*mat_row)
# print("Bunny position:", b_row, b_col)

max_direction = ""
max_eggs = -maxsize
max_moves = []

for direction, move in bunny_moves.items():
	eggs = 0
	current_egg_track = []
	row = b_row + move[0]
	col = b_col + move[1]

	while 0 <= row < rows and 0 <= col < rows:
		if matrix[row][col] == 'X':
			break

		eggs += int(matrix[row][col])
		current_egg_track.append([row, col])
		row += move[0]
		col += move[1]

	if eggs > max_eggs and current_egg_track:
		max_eggs = eggs
		max_direction = direction
		max_moves = current_egg_track

print(max_direction)
for mat_row in max_moves:
	print(mat_row)

print(max_eggs)
