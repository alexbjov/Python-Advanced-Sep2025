def insertion(data: list[int]):
	for j in range(1, len(data)):
		for i in range(j, 0, -1):
			if data[i] < data[i - 1]:
				data[i], data[i - 1] = data[i - 1], data[i]
			else:
				break


nums: list[int] = [int(x) for x in input().split()]
insertion(nums)
print(*nums)
