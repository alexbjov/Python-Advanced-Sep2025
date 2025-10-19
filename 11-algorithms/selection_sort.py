def selection(data: list[int]):
	for idx in range(len(data)):
		min_idx = idx
		
		for curr_idx in range(idx + 1, len(data)):
			if data[curr_idx] < data[min_idx]:
				min_idx = curr_idx
		
		data[idx], data[min_idx] = data[min_idx], data[idx]


nums: list[int] = [int(x) for x in input().split()]
selection(nums)
print(*nums)
