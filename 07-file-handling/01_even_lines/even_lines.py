import re

symbols = {"-", ",", ".", "!", "?"}
with open("text.txt") as file:
	lines = file.readlines()
	for i in range(0, len(lines), 2):
		even_line = reversed(re.sub('[-,.!?]', "@", lines[i]).split())
		print(" ".join(even_line))
