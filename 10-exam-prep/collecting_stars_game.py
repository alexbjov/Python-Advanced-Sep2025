n = int(input())
target = 10
collected_stars = 2
has_won = False

matrix = []
player_position = [-1, -1]
for i in range(n):
	row_data = [x for x in input().split()]
	if 'P' in row_data:
		j = row_data.index('P')
		player_position = [i, j]
	matrix.append(row_data)

moves = {
	"up": (-1, 0),
	"down": (1, 0),
	"left": (0, -1),
	"right": (0, 1)
}

while True:
	cmd = input()
	if not cmd:
		break

	next_move = moves[cmd]
	new_position_x = player_position[0] + next_move[0]
	new_position_y = player_position[1] + next_move[1]

	if not 0 <= new_position_x < n or not 0 <= new_position_y < n:
		new_position_x = 0
		new_position_y = 0

	if matrix[new_position_x][new_position_y] == '*':
		collected_stars += 1

	elif matrix[new_position_x][new_position_y] == '#':
		collected_stars -= 1

	if matrix[new_position_x][new_position_y] != '#':
		matrix[player_position[0]][player_position[1]] = '.'
		matrix[new_position_x][new_position_y] = 'P'
		player_position = [new_position_x, new_position_y]

	if collected_stars == target:
		has_won = True
		break

	if collected_stars == 0:
		break

if has_won:
	print(f"You won! You have collected {collected_stars} stars.")
else:
	print("Game over! You are out of any stars.")

print(f"Your final position is [{player_position[0]}, {player_position[1]}]")

for mat_row in matrix:
	print(*mat_row)
