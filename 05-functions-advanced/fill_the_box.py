def fill_the_box(*args):
	volume = 1
	cubes = 0
	for i in range(len(args)):
		if i <= 2:
			volume *= args[i]
			continue

		if args[i] == 'Finish':
			break

		cubes += args[i]

	if volume > cubes:
		return (f"There is free space in the box. "
				f"You could put {volume - cubes} more cubes.")

	return f"No more free space! You have {cubes - volume} more cubes."

# print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))

# print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))

print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
