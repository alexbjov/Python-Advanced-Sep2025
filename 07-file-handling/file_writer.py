import os

path = os.path.join("lab_files", "my_first_file.txt")

with open(path, 'w') as file:
	file.write('I just created my first file!')
