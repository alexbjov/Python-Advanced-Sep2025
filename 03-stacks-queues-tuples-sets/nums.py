first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())

num_of_lines = int(input())

for _ in range(num_of_lines):
	line = input().split()
	command = line[0] + ' ' + line[1]
	nums = list(map(int, line[2:]))

	if command == 'Add First':
		first_set.update(nums)
	elif command == 'Add Second':
		second_set.update(nums)
	elif command == 'Remove First':
		first_set.difference_update(nums)
	elif command == 'Remove Second':
		second_set.difference_update(nums)
	elif command == 'Check Subset':
		print(first_set.issubset(second_set) or second_set.issubset(first_set))

print(*sorted(first_set), sep=', ')
print(*sorted(second_set), sep=', ')
