nums = input().split()
nums_stack = []

while nums:
	nums_stack.append(nums.pop())

print(" ".join(nums_stack))
