num_of_names = int(input())
even_nums = set()
odd_nums = set()

for idx in range(num_of_names):
	name = input()
	sum_of_chars = 0

	for character in name:
		sum_of_chars += ord(character)

	result = sum_of_chars // (idx + 1)

	if result % 2 == 0:
		even_nums.add(result)
	else:
		odd_nums.add(result)

final_list = None
if sum(even_nums) == sum(odd_nums):
	final_list = list(even_nums.union(odd_nums))
elif sum(even_nums) < sum(odd_nums):
	final_list = list(odd_nums.difference(even_nums))
elif sum(even_nums) > sum(odd_nums):
	final_list = list(even_nums.symmetric_difference(odd_nums))

print(", ".join([str(num) for num in final_list]))
