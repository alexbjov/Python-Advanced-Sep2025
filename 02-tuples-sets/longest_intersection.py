num_of_lines = int(input())
max_length = 0
longest_set = None

for _ in range(num_of_lines):
	range1, range2 = input().split('-')
	a, b = [int(x) for x in range1.split(',')]
	c, d = [int(x) for x in range2.split(',')]

	set1 = set(list(range(a, b + 1)))
	set2 = set(list(range(c, d + 1)))

	common_set = set1.intersection(set2)
	if len(common_set) > max_length:
		max_length = len(common_set)
		longest_set = common_set

print(f"Longest intersection is {list(longest_set)} with length {max_length}")
