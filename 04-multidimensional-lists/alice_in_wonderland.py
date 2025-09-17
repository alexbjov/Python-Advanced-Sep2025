rows = int(input())

matrix = []
alice_pos_x, alice_pos_y = -1, -1
alice_moves = {
	"up": (-1, 0),
	"down": (1, 0),
	"left": (0, -1),
	"right": (0, 1)
}

for row in range(rows):
	matrix.append(input().split())
	for col in range(rows):
		if matrix[row][col] == 'A':
			alice_pos_x, alice_pos_y = row, col

# print("Alice:", alice_pos_x, alice_pos_y)
# for mat_row in matrix:
# 	print(*mat_row)

tea_sum = 0
has_won = False
has_left = False
has_died = False

while True:
	cmd = input()
	move = alice_moves[cmd]
	new_alice_pos_x = alice_pos_x + move[0]
	new_alice_pos_y = alice_pos_y + move[1]

	if not (0 <= new_alice_pos_x < rows and 0 <= new_alice_pos_y < rows):
		matrix[alice_pos_x][alice_pos_y] = '*'
		has_left = True
		break

	if matrix[new_alice_pos_x][new_alice_pos_y] == 'R':
		matrix[alice_pos_x][alice_pos_y] = '*'
		matrix[new_alice_pos_x][new_alice_pos_y] = '*'
		has_died = True
		break

	if (matrix[new_alice_pos_x][new_alice_pos_y]).isdigit():
		tea_sum += int(matrix[new_alice_pos_x][new_alice_pos_y])

	matrix[alice_pos_x][alice_pos_y] = '*'
	matrix[new_alice_pos_x][new_alice_pos_y] = "*"

	if tea_sum >= 10:
		has_won = True
		break

	alice_pos_x, alice_pos_y = new_alice_pos_x, new_alice_pos_y

if has_died or has_left:
	print("Alice didn't make it to the tea party.")
elif has_won:
	print("She did it! She went to the party.")

for mat_row in matrix:
	print(*mat_row)
