rows = int(input())
commands = [x for x in input().split()]

cmds_dict = {
	"left": lambda r, c: (r, c - 1),
	"right": lambda r, c: (r, c + 1),
	"up": lambda r, c: (r - 1, c),
	"down": lambda r, c: (r + 1, c)
}

matrix = []
miner_x, miner_y = -1, -1
for i in range(rows):
	row_data = [x for x in input().split()]
	matrix.append(row_data)
	if 's' in row_data:
		miner_x = i
		miner_y = row_data.index('s')

has_lost = False
counter = 0

for cmd in commands:
	new_miner_x, new_miner_y = cmds_dict[cmd](miner_x, miner_y)
	if 0 <= new_miner_x < rows:
		miner_x = new_miner_x
	if 0 <= new_miner_y < rows:
		miner_y = new_miner_y

	if matrix[miner_x][miner_y] == 'c':
		matrix[miner_x][miner_y] = '*'
	elif matrix[miner_x][miner_y] == 'e':
		has_lost = True
		break

else:
	for mat_row in matrix:
		counter += mat_row.count('c')

if has_lost:
	print(f"Game over! ({miner_x}, {miner_y})")
elif counter == 0:
	print(f"You collected all coal! ({miner_x}, {miner_y})")
else:
	print(f"{counter} pieces of coal left. ({miner_x}, {miner_y})")
