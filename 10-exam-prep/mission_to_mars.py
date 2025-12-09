n = int(input())
health = 100
spy_pos_x, spy_pos_y = -1, -1

matrix = []
for i in range(n):
	row_data = list(input())
	matrix.append(row_data)
	if "S" in row_data:
		j = row_data.index("S")
		spy_pos_x, spy_pos_y = i, j

moves_mapper = {
	"up": (-1, 0),
	"down": (1, 0),
	"left": (0, -1),
	"right": (0, 1)
}

is_mission_successful = False
while True:
	direction = input()
	if not direction:
		break
	
	move = moves_mapper[direction]
	
	new_spy_pos_x = spy_pos_x + move[0]
	new_spy_pos_y = spy_pos_y + move[1]
	
	if not 0 <= new_spy_pos_x < n or not 0 <= new_spy_pos_y < n:
		continue
	
	if matrix[new_spy_pos_x][new_spy_pos_y] == "G":
		health -= 40
		if health <= 0:
			matrix[spy_pos_x][spy_pos_y] = "."
			matrix[new_spy_pos_x][new_spy_pos_y] = "S"
			break
	
	elif matrix[new_spy_pos_x][new_spy_pos_y] == "E":
		matrix[spy_pos_x][spy_pos_y] = "."
		is_mission_successful = True
		break
	
	elif matrix[new_spy_pos_x][new_spy_pos_y] == "B":
		health = min(health + 15, 100)
	
	matrix[spy_pos_x][spy_pos_y] = "."
	matrix[new_spy_pos_x][new_spy_pos_y] = "S"
	spy_pos_x, spy_pos_y = new_spy_pos_x, new_spy_pos_y

if is_mission_successful:
	print("Mission accomplished. Spy extracted successfully.")
else:
	print("Mission failed. Spy compromised.")

print(f"Stealth level: {health} units")

for mat_row in matrix:
	print("".join(mat_row))
