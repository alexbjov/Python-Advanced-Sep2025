n = int(input())

space_field = []
resources = 100

ship_x = -1
ship_y = -1
for i in range(n):
	row_data = input().split()
	if 'S' in row_data:
		j = row_data.index('S')
		ship_x = i
		ship_y = j

	# print(*row_data)
	space_field.append(row_data)

moves = {
	"up": (-1, 0),
	"down": (1, 0),
	"left": (0, -1),
	"right": (0, 1)
}

has_died = False
has_failed = False
is_out = False

while True:
	cmd = input()
	if not cmd:
		break

	ship_moves = moves[cmd]
	new_ship_x = ship_x + ship_moves[0]
	new_ship_y = ship_y + ship_moves[1]

	resources -= 5

	if not 0 <= new_ship_x < n or not 0 <= new_ship_y < n:
		is_out = True
		break

	if space_field[new_ship_x][new_ship_y] == 'R':

		resources += 10
		if resources > 100:
			resources = 100

		if space_field[ship_x][ship_y] == 'RS':
			space_field[ship_x][ship_y] = 'R'
		else:
			space_field[ship_x][ship_y] = '.'

		space_field[new_ship_x][new_ship_y] = 'RS'

	elif space_field[new_ship_x][new_ship_y] == 'M':
		resources -= 5

		if space_field[ship_x][ship_y] == 'RS':
			space_field[ship_x][ship_y] = 'R'
		else:
			space_field[ship_x][ship_y] = '.'

		space_field[new_ship_x][new_ship_y] = 'S'

		if resources < 5:
			has_failed = True
			if resources <= 0:
				has_died = True
				break
			break

	elif space_field[new_ship_x][new_ship_y] == 'P':

		if space_field[ship_x][ship_y] == 'RS':
			space_field[ship_x][ship_y] = 'R'
		else:
			space_field[ship_x][ship_y] = '.'

		break

	elif space_field[new_ship_x][new_ship_y] == '.':

		if space_field[ship_x][ship_y] == 'RS':
			space_field[ship_x][ship_y] = 'R'
		else:
			space_field[ship_x][ship_y] = '.'
		space_field[new_ship_x][new_ship_y] = 'S'

		if resources < 5:
			has_failed = True
			if resources <= 0:
				has_died = True
				break
			break

	ship_x, ship_y = new_ship_x, new_ship_y

if is_out:
	print(f"Mission failed! The spaceship was lost in space.")
elif not has_died and not has_failed:
	print(f"Mission accomplished! The spaceship reached Planet B with {resources} resources left.")
elif has_died or has_failed:
	print(f"Mission failed! The spaceship was stranded in space.")

for space_row in space_field:
	print(*space_row)
