import os

path_to_file = os.path.join('lab_files', 'text.txt')
try:
	open(path_to_file)
	print("File found")

except FileNotFoundError:
	print("File not found")
