def spread_bunnies(mat, set_bunnies):
	new_bunnies_set = set()
	directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	for b_row, b_col in set_bunnies:
		for d_row, d_col in directions:
			new_row, new_col = b_row + d_row, b_col + d_col
			if 0 <= new_row < len(mat) and 0 <= new_col < len(mat[0]):
				mat[new_row][new_col] = 'B'
				new_bunnies_set.add((new_row, new_col))

	return mat, set_bunnies.union(new_bunnies_set)


rows, cols = [int(x) for x in input().split()]

matrix = []
p_row, p_col = 0, 0
bunnies_set = set()

for row in range(rows):
	row_data = [x for x in input()]
	matrix.append(row_data)
	for col in range(cols):
		if matrix[row][col] == 'P':
			p_row, p_col = row, col
		elif matrix[row][col] == 'B':
			bunnies_set.add((row, col))

commands = list(input())

moves = {
	"U": lambda r, c: (r - 1, c),
	"D": lambda r, c: (r + 1, c),
	"L": lambda r, c: (r, c - 1),
	"R": lambda r, c: (r, c + 1)
}

has_won = False
for cmd in commands:
	new_p_row, new_p_col = moves[cmd](p_row, p_col)
	matrix, bunnies_set = spread_bunnies(matrix, bunnies_set)
	if (p_row, p_col) not in bunnies_set:
		matrix[p_row][p_col] = '.'

	if (new_p_row < 0 or new_p_row >= rows or new_p_col < 0 or new_p_col
			>= cols):
		has_won = True
		break

	p_row, p_col = new_p_row, new_p_col
	if matrix[p_row][p_col] == 'B':
		break

for row in matrix:
	print("".join(row))

if has_won:
	print(f"won: {p_row} {p_col}")
else:
	print(f"dead: {p_row} {p_col}")
