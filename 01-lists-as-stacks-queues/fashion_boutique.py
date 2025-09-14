clothes_stack = list(map(int, input().split()))
rack_capacity = int(input())
racks = 1
rack_sum = 0

while clothes_stack:
	clothes = clothes_stack.pop()
	if rack_sum + clothes <= rack_capacity:
		rack_sum += clothes
	else:
		rack_sum = clothes
		racks += 1

print(racks)
