main_colors = {"red", "yellow", "blue"}
secondary_colors = {
	"orange": {"red", "yellow"},
	"purple": {"red", "blue"},
	"green": {"yellow", "blue"}
}

colors = []
words_list = input().split()

while True:
	if not words_list:
		break

	word1 = words_list[0]
	word2 = words_list[-1]
	potential_color_1 = (word1 + word2).strip()
	potential_color_2 = (word2 + word1).strip()
	if len(words_list) == 1:
		mid_point = len(colors) // 2
		if potential_color_1 in main_colors:
			colors.insert(mid_point, potential_color_1)
		elif potential_color_2 in main_colors:
			colors.insert(mid_point, potential_color_2)
		elif potential_color_1 in secondary_colors:
			clrs = secondary_colors[potential_color_1]
			for clr in clrs:
				if clr not in colors:
					break
			else:
				colors.insert(mid_point, potential_color_1)

		elif potential_color_2 in secondary_colors:
			clrs = secondary_colors[potential_color_2]
			for clr in clrs:
				if clr not in colors:
					break
			else:
				colors.insert(mid_point, potential_color_2)

	if potential_color_1 in main_colors:
		words_list = words_list[1:-1]
		mid_point = len(colors) // 2
		colors.insert(mid_point, potential_color_1)

	elif potential_color_2 in main_colors:
		words_list = words_list[1:-1]
		mid_point = len(colors) // 2
		colors.insert(mid_point, potential_color_2)

	elif potential_color_1 in secondary_colors:
		main_clrs = secondary_colors[potential_color_1]
		for clr in main_clrs:
			if clr not in colors:
				words_list = words_list[1:-1]
				mid_point = len(words_list) // 2
				words_list.insert(mid_point, potential_color_1)
				break
		else:
			words_list = words_list[1:-1]
			mid_point = len(colors) // 2
			colors.insert(mid_point, potential_color_1)

	elif potential_color_2 in secondary_colors:
		main_clrs = secondary_colors[potential_color_2]
		for clr in main_clrs:
			if clr not in colors:
				words_list = words_list[1:-1]
				mid_point = len(words_list) // 2
				words_list.insert(mid_point, potential_color_2)
				break
		else:
			words_list = words_list[1:-1]
			mid_point = len(colors) // 2
			colors.insert(mid_point, potential_color_2)

	else:
		words_list[0] = words_list[0][:-1]
		words_list[-1] = words_list[-1][:-1]

	print(colors)
