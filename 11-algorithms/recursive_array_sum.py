def calc_sum(arr: list[int], idx: int) -> int:
	if idx == len(arr) - 1:
		return arr[idx]
	
	return arr[idx] + calc_sum(arr, idx + 1)


my_array: list[int] = [int(x) for x in input().split()]
sum_of_items = calc_sum(my_array, 0)
print(sum_of_items)
