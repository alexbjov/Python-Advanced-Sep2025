rows = int(input())
pacman: list[int] = [-1, -1]
health = 100
total_stars = 0
collected_stars = 0
has_immunity: bool = False

matrix = []
for i in range(rows):
	row_data = list(input())
	matrix.append(row_data)
	if 'P' in row_data:
		j = row_data.index('P')
		pacman = [i, j]
		matrix[i][j] = '-'
	
	elif '*' in row_data:
		total_stars += row_data.count('*')

pacman_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
	command = input()
	if command == 'end':
		print("Pacman failed to collect all the stars.")
		break
	
	move = pacman_moves[command]
	new_x = (pacman[0] + move[0]) % rows
	new_y = (pacman[1] + move[1]) % rows
	
	if matrix[new_x][new_y] == 'G':
		matrix[new_x][new_y] = '-'
		if not has_immunity:
			health -= 50
			if health <= 0:
				pacman = [new_x, new_y]
				print(f"Game over! Pacman last coordinates [{new_x},{new_y}]")
				break
		
		has_immunity = False
	
	elif matrix[new_x][new_y] == 'F':
		matrix[new_x][new_y] = '-'
		has_immunity = True
	
	elif matrix[new_x][new_y] == '*':
		matrix[new_x][new_y] = '-'
		collected_stars += 1
		if collected_stars == total_stars:
			pacman = [new_x, new_y]
			print("Pacman wins! All the stars are collected.")
			break
	
	pacman = [new_x, new_y]

print(f"Health: {health}")
if total_stars > collected_stars:
	print(f"Uncollected stars: {total_stars - collected_stars}")

matrix[pacman[0]][pacman[1]] = 'P'
for mat_row in matrix:
	print(*mat_row, sep="")
