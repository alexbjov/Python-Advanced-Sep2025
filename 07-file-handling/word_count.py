import os
import re

with open(os.path.join("lab_files", "input.txt")) as file:
	text = file.read()

with open(os.path.join("lab_files", "words.txt")) as file:
	words = file.read().split()

data = {}
for word in words:
	pattern = rf'\b{word}\b'
	count = len(re.findall(pattern, text, re.IGNORECASE))
	data[word] = count

sorted_data = sorted(data.items(), key=lambda kvp: -kvp[1])

for word, count in sorted_data:
	print(f'{word} - {count}')
