from wsgiref.util import application_uri

matrix = []

my_pos_x, my_pos_y = -1, -1
for row in range(5):
	row_data = input().split()
	matrix.append(row_data)
	# print(*row_data)
	for col in range(5):
		if matrix[row][col] == "A":
			my_pos_x, my_pos_y = row, col

# print("My position:", my_pos_x, my_pos_y)
my_moves = {
	"up": (-1, 0),
	"down": (1, 0),
	"left": (0, -1),
	"right": (0, 1)
}

my_shots = {
	"up": (-1, 0),
	"down": (1, 0),
	"left": (0, -1),
	"right": (0, 1)
}

targets = []
targets_left_counter = 0

num_of_cmds = int(input())
for _ in range(num_of_cmds):
	tokens = input().split()
	action = tokens[0]
	direction = tokens[1]

	if action == 'move':
		steps_to_move = int(tokens[2])
		moves_coords = my_moves[direction]
		new_pos_x = my_pos_x + moves_coords[0]
		new_pos_y = my_pos_y + moves_coords[1]
		matrix[my_pos_x][my_pos_y] = '.'
		counter = 0
		while 0 <= new_pos_x < 5 and 0 <= new_pos_y < 5 and counter < steps_to_move:
			matrix[my_pos_x][my_pos_y] = '.'
			if matrix[new_pos_x][new_pos_y] == 'x':
				break
			my_pos_x = new_pos_x
			my_pos_y = new_pos_y
			new_pos_x = my_pos_x + moves_coords[0]
			new_pos_y = my_pos_y + moves_coords[1]
			counter += 1

	elif action == 'shoot':
		matrix[my_pos_x][my_pos_y] = '.'
		start_pos_x = my_pos_x
		start_pos_y = my_pos_y
		shot_coords = my_shots[direction]
		next_pos_x = start_pos_x + shot_coords[0]
		next_pos_y = start_pos_y + shot_coords[1]
		while (0 <= next_pos_x < 5 and 0 <= next_pos_y < 5):
			if matrix[next_pos_x][next_pos_y] == 'x':
				targets.append([next_pos_x, next_pos_y])
				matrix[next_pos_x][next_pos_y] = '.'
				break

			start_pos_x, start_pos_y = next_pos_x, next_pos_y
			next_pos_x = start_pos_x + shot_coords[0]
			next_pos_y = start_pos_y + shot_coords[1]

for mat_row in matrix:
	targets_left_counter += mat_row.count('x')
	# print("Counter on each row:", targets_left_counter)

if targets_left_counter == 0:
	print(f"Training completed! All {len(targets)} targets hit.")
else:
	print(f"Training not completed! {targets_left_counter} targets left.")

if targets:
	for target_row in targets:
		print(target_row)
