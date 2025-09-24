SIZE = 5
matrix = []
my_position = []
targets = 0
for row in range(SIZE):
	row_data = input().split()
	matrix.append(row_data)
	for col in range(SIZE):
		if matrix[row][col] == "A":
			my_position = [row, col]
		elif matrix[row][col] == 'x':
			targets += 1

my_moves = {
	"up": (-1, 0),
	"down": (1, 0),
	"left": (0, -1),
	"right": (0, 1)
}

hit_targets = []

num_of_commands = int(input())
for _ in range(num_of_commands):
	command = input().split()
	action = command[0]
	direction = command[1]
	move = my_moves[direction]
	if action == 'shoot':
		next_row = my_position[0] + move[0]
		next_col = my_position[1] + move[1]
		
		while 0 <= next_row < SIZE and 0 <= next_col < SIZE:
			if matrix[next_row][next_col] == 'x':
				hit_targets.append([next_row, next_col])
				matrix[next_row][next_col] = '.'
				break
			
			next_row += move[0]
			next_col += move[1]
		
		if targets == len(hit_targets):
			print(f"Training completed! All {targets} targets hit.")
			break
	
	elif action == 'move':
		steps = int(command[2])
		next_row = my_position[0] + move[0] * steps
		next_col = my_position[1] + move[1] * steps
		
		if (0 <= next_row < SIZE and 0 <= next_col < SIZE and
				matrix[next_row][next_col] == '.'):
			my_position = [next_row, next_col]

if targets > len(hit_targets):
	print(f"Training not completed! "
		  f"{targets - len(hit_targets)} targets left.")

for coordinates in hit_targets:
	print(coordinates)
