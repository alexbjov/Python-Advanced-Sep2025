import os

try:
	path = os.path.join('lab_files', "my_first_file.txt")
	os.remove(path)
except FileNotFoundError:
	print("File already deleted!")
