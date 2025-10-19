def bin_search(data: list[int], item: int) -> int:
	left = 0
	right = len(data) - 1
	
	while left <= right:
		mid: int = (left + right) // 2
		mid_el = data[mid]
		if item == mid_el:
			return mid
		elif item > mid_el:
			left = mid + 1
		else:
			right = mid
	
	return -1


my_arr: list[int] = [int(x) for x in input().split()]
target = int(input())
print(bin_search(my_arr, target))
