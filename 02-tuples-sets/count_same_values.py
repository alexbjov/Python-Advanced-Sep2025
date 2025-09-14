nums = tuple([float(x) for x in input().split()])

data = {}
for num in nums:
	if num not in data:
		data[num] = nums.count(num)

for num, count in data.items():
	print(f"{num:.1f} - {count} times")
