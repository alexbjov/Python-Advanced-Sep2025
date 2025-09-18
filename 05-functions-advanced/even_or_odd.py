def even_odd(*args):
	result = []
	cmd = args[-1]
	for i in range(len(args) - 1):
		if cmd == 'even' and args[i] % 2 == 0:
			result.append(args[i])
		elif cmd == 'odd' and args[i] % 2 != 0:
			result.append(args[i])
	return result

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
