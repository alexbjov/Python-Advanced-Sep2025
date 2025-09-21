from string import punctuation

with open("text.txt") as input_file, open("output.txt", "w") as output_file:
	result = []
	line_counter = 1
	for line in input_file.readlines():
		counter_alpha = 0
		counter_special = 0
		for character in line:
			if character.isalpha():
				counter_alpha += 1
			elif character in punctuation:
				counter_special += 1

		result.append(f"Line {line_counter}: {line.strip()} ({counter_alpha})({counter_special})")
		line_counter += 1

	output_file.write("\n".join(result))
