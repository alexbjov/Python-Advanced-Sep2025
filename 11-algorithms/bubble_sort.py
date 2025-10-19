def bubble(data: list[int]):
	is_sorted: bool = False
	sorted_elems = 0
	
	while not is_sorted:
		is_sorted = True
		
		for j in range(1, len(data) - sorted_elems):
			i = j - 1
			if data[i] > data[j]:
				data[i], data[j] = data[j], data[i]
				is_sorted = False
		
		sorted_elems += 1


nums = [int(x) for x in input().split()]
bubble(nums)
print(*nums)
