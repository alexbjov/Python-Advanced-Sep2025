from collections import deque

main_colors = ["red", "yellow", "blue"]
secondary_colors = {"orange": ["red", "yellow"], "purple": ["red", "blue"],
					"green": ["yellow", "blue"]}

collected_colors = []
colors_queue = deque(input().split())

while colors_queue:
	first_str = colors_queue.popleft()
	last_str = colors_queue.pop() if colors_queue else ""
	
	for color in (first_str + last_str, last_str + first_str):
		if color in main_colors or color in secondary_colors:
			collected_colors.append(color)
			break
	
	else:
		first_sub = first_str[:-1] if first_str else ""
		last_sub = last_str[:-1] if last_str else ""
		
		mid_idx = len(colors_queue) // 2
		
		if first_sub:
			colors_queue.insert(mid_idx, first_sub)
		
		if last_sub:
			colors_queue.insert(mid_idx, last_sub)

final_colors = []
for color in collected_colors:
	if color in secondary_colors:
		req_colors = secondary_colors[color]
		if all(main_clr in collected_colors for main_clr in req_colors):
			final_colors.append(color)
	
	else:
		final_colors.append(color)

print(final_colors)
