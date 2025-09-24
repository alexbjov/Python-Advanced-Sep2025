m_presents = int(input())
n_neighbourhood = int(input())
santa = [-1, -1]
total_nice_kids = 0

matrix = []
for row in range(n_neighbourhood):
	row_data = input().split()
	matrix.append(row_data)
	
	for col in range(n_neighbourhood):
		if matrix[row][col] == 'S':
			santa = [row, col]
		elif matrix[row][col] == 'V':
			total_nice_kids += 1

possible_moves = {
	"up": (-1, 0),
	"down": (1, 0),
	"left": (0, -1),
	"right": (0, 1)
}

nice_kids_gifted = 0
presents_given = 0
while m_presents > presents_given:
	cmd = input()
	if cmd == 'Christmas morning':
		break
	
	move = possible_moves[cmd]
	next_row = santa[0] + move[0]
	next_col = santa[1] + move[1]
	
	if not (0 <= next_row < n_neighbourhood and
			0 <= next_col < n_neighbourhood):
		continue
	
	if matrix[next_row][next_col] == 'V':
		nice_kids_gifted += 1
		presents_given += 1
	
	if matrix[next_row][next_col] == 'C':
		for santa_moves in possible_moves.values():
			adj_row = next_row + santa_moves[0]
			adj_col = next_col + santa_moves[1]
			if matrix[adj_row][adj_col] in 'XV':
				if m_presents > presents_given:
					if matrix[adj_row][adj_col] == 'V':
						nice_kids_gifted += 1
					presents_given += 1
			
			matrix[adj_row][adj_col] = '-'
	
	matrix[santa[0]][santa[1]] = '-'
	matrix[next_row][next_col] = 'S'
	santa = [next_row, next_col]

if m_presents == presents_given and total_nice_kids > nice_kids_gifted:
	print("Santa ran out of presents!")

for mat_row in matrix:
	print(*mat_row)

if total_nice_kids == nice_kids_gifted:
	print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
else:
	print(f"No presents for {total_nice_kids - nice_kids_gifted} nice kid/s.")
