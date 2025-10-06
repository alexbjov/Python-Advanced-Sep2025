def check_row_winner(my_board, curr_sign) -> bool:
	for r in my_board:
		if r.count(curr_sign) == 3:
			return True
	
	return False


def check_col_winner(my_board, curr_sign) -> bool:
	for col_idx in range(3):
		counter = 0
		for row_idx in range(3):
			if my_board[row_idx][col_idx] == curr_sign:
				counter += 1
		
		if counter == 3:
			return True
	
	return False


def check_diagonal_winner(my_board, curr_sign) -> bool:
	counter_primary = 0
	counter_secondary = 0
	for idx in range(3):
		if my_board[idx][idx] == curr_sign:
			counter_primary += 1
		if my_board[idx][3 - idx - 1] == curr_sign:
			counter_secondary += 1
	
	if counter_primary == 3 or counter_secondary == 3:
		return True
	
	return False


def check_for_winner(my_board, curr_sign) -> bool:
	if (check_row_winner(my_board, curr_sign) or check_col_winner(my_board,
			curr_sign) or check_diagonal_winner(my_board, curr_sign)):
		return True
	
	return False


def draw_board(my_board):
	for r in my_board:
		print(f"| {' | '.join(r)} |")


board = [[" ", " ", " "] for _ in range(3)]
mapper = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2),
		  7: (2, 0), 8: (2, 1), 9: (2, 2)}

player_1_name = input("Player 1 name: ")
player_2_name = input("Player 2 name: ")
player_1_sign = input(
	f"{player_1_name} would you like to play with 'X' or 'O'? ").upper()

while player_1_sign not in ['X', 'O']:
	print("Please enter either 'X' or 'O'")
	player_1_sign = input(
		f"{player_1_name} would you like to play with 'X' or 'O'? ").upper()

player_2_sign = 'O' if player_1_sign == 'X' else 'X'

print('This is the numeration of the board:')
print('| 1 | 2 | 3 |')
print('| 4 | 5 | 6 |')
print('| 7 | 8 | 9 |')

print(f"{player_1_name} starts first")

turn = 1
while turn < 10:
	current_player = player_1_name if turn % 2 != 0 else player_2_name
	current_sign = player_1_sign if turn % 2 != 0 else player_2_sign
	
	try:
		position = int(input(
			f"{current_player} please choose a free position between [1-9]: "))
	except ValueError:
		print("Please enter a valid number.")
		continue
	
	if not (1 <= position <= 9):
		print("Please enter a valid number.")
		continue
	
	row, col = mapper[position]
	if board[row][col] != " ":
		print("This position is already occupied!")
		continue
	
	board[row][col] = current_sign
	
	if turn >= 5:
		is_winner = check_for_winner(board, current_sign)
		if is_winner:
			print(f"Congratulations, {current_player} won!")
			break
	
	turn += 1
	draw_board(board)

else:
	print("No one is winner!")
