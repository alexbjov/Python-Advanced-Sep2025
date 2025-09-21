import os

line = input()
while line != 'End':
	command, filename, *args = line.split('-')

	if command == 'Create':
		open(filename, "w").close()

	elif command == 'Add':
		content = args[0]
		with open(filename, "a") as file:
			file.write(f'{content}\n')

	elif command == "Replace":
		old_str = args[0]
		new_str = args[1]
		try:
			with open(filename, 'r+') as file:
				content = file.read()
				file.seek(0)
				file.truncate(0)
				file.write(content.replace(old_str, new_str))
		except FileNotFoundError:
			print("An error occurred")

	elif command == 'Delete':
		if os.path.exists(filename):
			os.remove(filename)
		else:
			print("An error occurred")
	line = input()
