n = int(input())
matrix = []
num_of_enemies = 4
jet_fighter = [-1, -1]
for i in range(n):
	row_data = input()
	matrix.append([x for x in row_data])
	if 'J' in row_data:
		j = row_data.index('J')
		jet_fighter = [i, j]

jet_moves = {
	"up": (-1, 0),
	"down": (1, 0),
	"left": (0, -1),
	"right": (0, 1)
}

armor_value = 300
enemies_hit = 0
mission_won = False

while armor_value > 0 and num_of_enemies > enemies_hit:
	cmd = input()
	if not cmd:
		break
	
	moves = jet_moves[cmd]
	new_row = jet_fighter[0] + moves[0]
	new_col = jet_fighter[1] + moves[1]
	
	if matrix[new_row][new_col] == 'E':
		if num_of_enemies > enemies_hit + 1:
			armor_value -= 100
			if armor_value > 0:
				enemies_hit += 1
		
		else:
			enemies_hit = num_of_enemies
	
	
	elif matrix[new_row][new_col] == 'R':
		armor_value = 300
	
	matrix[jet_fighter[0]][jet_fighter[1]] = '-'
	matrix[new_row][new_col] = 'J'
	jet_fighter = [new_row, new_col]

if num_of_enemies == enemies_hit:
	print("Mission accomplished, you neutralized the aerial threat!")
else:
	print(
		f"Mission failed, your jetfighter was shot down! Last coordinates ["
		f"{jet_fighter[0]}, {jet_fighter[1]}]!")

for mat_row in matrix:
	print("".join(mat_row))
