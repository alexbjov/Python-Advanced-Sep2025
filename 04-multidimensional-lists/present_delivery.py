m_presents = int(input())
n_neighbourhood = int(input())
santa_x, santa_y = -1, -1

matrix = []
for row in range(n_neighbourhood):
	row_data = input().split()
	matrix.append(row_data)
	# print(*row_data)
	for col in range(n_neighbourhood):
		if matrix[row][col] == 'S':
			santa_x, santa_y = row, col

possible_moves = {
	"up": (-1, 0),
	"down": (1, 0),
	"left": (0, -1),
	"right": (0, 1)
}

presents_given = 0
while m_presents > presents_given:
	cmd = input()
	if cmd == 'Christmas morning':
		break

	move_x, move_y = possible_moves[cmd]
	new_santa_x = santa_x + move_x
	new_santa_y = santa_y + move_y

	if not(0 <= new_santa_x < n_neighbourhood and
		   0 <= new_santa_y < n_neighbourhood):
		continue

	if matrix[new_santa_x][new_santa_y] == 'V':
		presents_given += 1
	elif matrix[new_santa_x][new_santa_y] == 'C':
		matrix[santa_x][santa_y] = '-'

		for moves_coords in possible_moves.values():
			next_move_x = new_santa_x + moves_coords[0]
			next_move_y = new_santa_y + moves_coords[1]
			if (0 <= next_move_x < n_neighbourhood and
					0 <= next_move_y < n_neighbourhood):

				if (matrix[next_move_x][next_move_y] == 'X' or
					matrix[next_move_x][next_move_y] == 'V'):

					if m_presents > presents_given:
						matrix[next_move_x][next_move_y] = '-'
						presents_given += 1

	matrix[santa_x][santa_y] = '-'
	matrix[new_santa_x][new_santa_y] = 'S'
	santa_x = new_santa_x
	santa_y = new_santa_y

nice_kids_left = 0
for mat_row in matrix:
	nice_kids_left += mat_row.count('V')

if nice_kids_left and m_presents == presents_given:
	print("Santa ran out of presents!")

for mat_row in matrix:
	print(*mat_row)

if nice_kids_left == 0:
	print(f"Good job, Santa! {presents_given} happy nice kid/s.")
else:
	print(f"No presents for {nice_kids_left} nice kid/s")
