n = int(input())

health = 100
damage = 40
health_boost = 15
has_found_exit = False
has_died = False

matrix = []
traveller_x, traveller_y = -1, -1

for i in range(n):
	row_data = [x for x in input()]
	if 'P' in row_data:
		traveller_x = i
		traveller_y = row_data.index('P')
	matrix.append(row_data)

traveler_moves = {
	"up": (-1, 0),
	"down": (1, 0),
	"left": (0, -1),
	"right": (0, 1)
}

while True:
	cmd = input()
	if not cmd:
		break

	moves = traveler_moves[cmd]
	new_traveller_x = traveller_x + moves[0]
	new_traveller_y = traveller_y + moves[1]

	if not 0 <= new_traveller_x < n or not 0 <= new_traveller_y < n:
		continue

	if matrix[new_traveller_x][new_traveller_y] == 'M':
		health -= damage
		matrix[traveller_x][traveller_y] = '-'
		matrix[new_traveller_x][new_traveller_y] = 'P'
		if health <= 0:
			health = 0
			has_died = True
			break

	elif matrix[new_traveller_x][new_traveller_y] == 'H':
		health += health_boost
		if health > 100:
			health = 100

	elif matrix[new_traveller_x][new_traveller_y] == 'X':
		matrix[traveller_x][traveller_y] = '-'
		matrix[new_traveller_x][new_traveller_y] = 'P'
		has_found_exit = True
		break

	matrix[traveller_x][traveller_y] = '-'
	matrix[new_traveller_x][new_traveller_y] = 'P'
	traveller_x = new_traveller_x
	traveller_y = new_traveller_y

if has_died:
	print("Player is dead. Maze over!")
elif has_found_exit:
	print("Player escaped the maze. Danger passed!")

print(f"Player's health: {health} units")
for mat_row in matrix:
	print("".join(mat_row))
