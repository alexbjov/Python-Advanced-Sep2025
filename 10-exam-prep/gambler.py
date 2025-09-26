n = int(input())
gambler = [-1, -1]
gambler_amount = 100
has_won = False

matrix = []
for i in range(n):
	row_data = [x for x in input()]
	matrix.append(row_data)
	if 'G' in row_data:
		j = row_data.index('G')
		gambler = [i, j]

gambler_moves = {
	"up": (-1, 0),
	"down": (1, 0),
	"left": (0, -1),
	"right": (0, 1)
}

direction = input()
while direction != 'end':
	moves = gambler_moves[direction]
	next_row = gambler[0] + moves[0]
	next_col = gambler[1] + moves[1]
	
	matrix[gambler[0]][gambler[1]] = '-'
	if not 0 <= next_row < n or not 0 <= next_col < n:
		print("Game over! You lost everything!")
		break
	
	if matrix[next_row][next_col] == 'W':
		gambler_amount += 100
	
	elif matrix[next_row][next_col] == 'P':
		gambler_amount -= 200
	
	elif matrix[next_row][next_col] == 'J':
		gambler_amount += 100_000
		matrix[next_row][next_col] = 'G'
		has_won = True
		break
	
	if gambler_amount <= 0:
		print("Game over! You lost everything!")
		break
	
	matrix[next_row][next_col] = 'G'
	gambler = [next_row, next_col]
	direction = input()

else:
	print(f"End of the game. Total amount: {gambler_amount}$")
	if gambler_amount > 0:
		for mat_row in matrix:
			print("".join(mat_row))

if has_won:
	print(f"You win the Jackpot!\nEnd of the game. Total amount: "
		  f"{gambler_amount}$")
	
	for mat_row in matrix:
		print("".join(mat_row))
