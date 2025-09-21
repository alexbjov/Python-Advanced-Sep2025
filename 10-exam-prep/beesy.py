n = int(input())

matrix = []
bee_x, bee_y = -1, -1
bee_energy = 15
honey_target = 30
honey_collected = 0
has_recharged = False
has_died = False
has_reached_hive = False

bee_moves = {
	"up": (-1, 0),
	"down": (1, 0),
	"left": (0, -1),
	"right": (0, 1)
}

for row in range(n):
	row_data = [x for x in input()]
	if 'B' in row_data:
		bee_x = row
		bee_y = row_data.index('B')
	matrix.append(row_data)
# print("".join(row_data))

while True:
	cmd = input()
	if not cmd:
		break

	move = bee_moves[cmd]
	new_bee_x = bee_x + move[0]
	new_bee_y = bee_y + move[1]

	if new_bee_x < 0:
		new_bee_x = n - 1
	elif new_bee_x > n - 1:
		new_bee_x = 0

	if new_bee_y < 0:
		new_bee_y = n - 1
	elif new_bee_y > n - 1:
		new_bee_y = 0

	if matrix[new_bee_x][new_bee_y].isdigit():
		honey_collected += int(matrix[new_bee_x][new_bee_y])

	matrix[bee_x][bee_y] = '-'
	bee_energy -= 1
	# print("Energy:", bee_energy)
	# print("Honey collected:", honey_collected)
	# print(f"(Bee_x, Bee_y)={(new_bee_x, new_bee_y)}")
	# print("-----------------------------------")
	if matrix[new_bee_x][new_bee_y] == 'H':
		matrix[new_bee_x][new_bee_y] = 'B'
		has_reached_hive = True
		break

	matrix[new_bee_x][new_bee_y] = 'B'
	if bee_energy == 0 and honey_collected < honey_target:
		has_died = True
		break
	elif bee_energy == 0 and honey_collected >= honey_target:
		if not has_recharged:
			bee_energy = honey_collected - honey_target
			honey_collected = honey_target
			has_recharged = True
		else:
			has_died = True
			break

	bee_x, bee_y = new_bee_x, new_bee_y

if has_reached_hive and honey_collected >= honey_target:
	print(f"Great job, Beesy! The hive is full. Energy left: {bee_energy}")
elif has_reached_hive and honey_collected < honey_target:
	print("Beesy did not manage to collect enough nectar.")
elif has_died and not has_reached_hive:
	print("This is the end! Beesy ran out of energy.")

for mat_row in matrix:
	print("".join(mat_row))
