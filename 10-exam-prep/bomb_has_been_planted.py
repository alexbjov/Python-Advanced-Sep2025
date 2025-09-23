n, m = map(int, input().split(', '))

counterterrorist_x, counterterrorist_y = -1, -1
matrix = []
for i in range(n):
	row_data = [x for x in input()]
	if 'C' in row_data:
		counterterrorist_x = i
		counterterrorist_y = row_data.index('C')
	matrix.append(row_data)

# print(f"CT coords: {counterterrorist_x}, {counterterrorist_y}")

ct_moves = {
	"up": (-1, 0),
	"down": (1, 0),
	"left": (0, -1),
	"right": (0, 1),
}

total_time = 16
has_defused_bomb = False
has_lost = False
counter = 0

while True:
	cmd = input()

	if not cmd:
		break

	total_time -= 1

	new_ct_x = counterterrorist_x
	new_ct_y = counterterrorist_y
	if cmd != 'defuse':
		moves = ct_moves[cmd]
		new_ct_x += moves[0]
		new_ct_y += moves[1]

	if not 0 <= new_ct_x < n or not 0 <= new_ct_y < m:
		continue

	if cmd == 'defuse' and matrix[new_ct_x][new_ct_y] != 'B':
		counterterrorist_x = new_ct_x
		counterterrorist_y = new_ct_y
		total_time -= 1
		if total_time <= 0:
			has_lost = True
			break

		continue

	if matrix[new_ct_x][new_ct_y] == 'B':
		if cmd != 'defuse' and counter == 0:
			counter += 1
			counterterrorist_x = new_ct_x
			counterterrorist_y = new_ct_y
			continue

		counter = 0
		if cmd == 'defuse':
			total_time -= 3
			if total_time >= 0:
				matrix[new_ct_x][new_ct_y] = 'D'
				has_defused_bomb = True

			else:
				matrix[new_ct_x][new_ct_y] = 'X'
				has_lost = True

			break

	if matrix[new_ct_x][new_ct_y] == 'T':
		matrix[new_ct_x][new_ct_y] = '*'
		has_lost = True
		break

	if total_time <= 0:
		has_lost = True
		break
	counterterrorist_x = new_ct_x
	counterterrorist_y = new_ct_y

if has_lost:
	print("Terrorists win!")

if not has_defused_bomb and total_time <= 0:
	print("Bomb was not defused successfully!")
	print(f"Time needed: {abs(total_time)} second/s.")

elif has_defused_bomb and total_time >= 0:
	print("Counter-terrorist wins!")
	print(f"Bomb has been defused: {total_time} second/s remaining.")

for mat_row in matrix:
	print("".join(mat_row))
