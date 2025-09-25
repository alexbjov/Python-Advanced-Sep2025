from collections import deque

main_colors = {"red", "yellow", "blue"}
secondary_colors = {
	"orange": {"red", "yellow"},
	"purple": {"red", "blue"},
	"green": {"yellow", "blue"}
}

all_colors = []
sec_colors = []
start_list = deque(input().split())

while len(start_list) > 1:
	
	first_word = start_list.pop()
	last_word = start_list.popleft()
	
	composed_word_1 = (first_word + last_word).strip()
	composed_word_2 = (last_word + first_word).strip()
	
	if composed_word_1 in main_colors:
		all_colors.append(composed_word_1)
	
	elif composed_word_1 in secondary_colors:
		position_to_add = len(all_colors)
		sec_colors.append((composed_word_1, position_to_add))
	
	elif composed_word_2 in main_colors:
		all_colors.append(composed_word_2)
	
	elif composed_word_2 in secondary_colors:
		position_to_add = len(all_colors)
		sec_colors.append((composed_word_2, position_to_add))
	
	else:
		mid_point = len(start_list) // 2
		new_word_1 = (first_word[:-1] + last_word[:-1]).strip()
		new_word_2 = (last_word[:-1] + first_word[:-1]).strip()
		if new_word_1 in main_colors:
			all_colors.append(new_word_1)
		
		elif new_word_1 in secondary_colors:
			position_to_add = len(all_colors)
			sec_colors.append((new_word_1, position_to_add))
		
		elif new_word_2 in main_colors:
			all_colors.append(new_word_2)
		
		elif new_word_2 in secondary_colors:
			position_to_add = len(all_colors)
			sec_colors.append((new_word_2, position_to_add))
		
		else:
			start_list.insert(mid_point, new_word_1)

if start_list:
	if start_list[0] in main_colors:
		all_colors.append(start_list[0])

for color, position in sec_colors:
	possible_main_colors = secondary_colors[color]
	for pos_main_clr in possible_main_colors:
		if pos_main_clr not in all_colors:
			break
	
	else:
		all_colors.insert(position, color)

print(all_colors)
