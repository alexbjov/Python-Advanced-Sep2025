from string import punctuation

with open("text.txt") as input_file, open("output.txt", "w") as output_file:
	result = []
	
	for line_counter, line in enumerate(input_file.readlines(), start=1):
		counter_alpha = 0
		counter_special = 0
		for character in line:
			if character.isalpha():
				counter_alpha += 1
			elif character in punctuation:
				counter_special += 1
		
		result.append(
			f"Line {line_counter}: {line.strip()} ({counter_alpha})({counter_special})\n")
	
	output_file.write("".join(result))
