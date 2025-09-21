from collections import deque

packages_stack = [int(x) for x in input().split()]
couriers_queue = deque([int(x) for x in input().split()])
delivered_weight = 0

while packages_stack and couriers_queue:
	package = packages_stack[-1]
	courier = couriers_queue.popleft()

	if courier >= package:
		delivered_weight += package
		packages_stack.pop()

		courier -= 2 * package
		if courier > 0:
			couriers_queue.append(courier)

	else:
		packages_stack[-1] -= courier
		delivered_weight += courier

print(f"Total weight: {delivered_weight} kg")
if not packages_stack and not couriers_queue:
	print("Congratulations, all packages were delivered successfully by the couriers today.")
elif packages_stack and not couriers_queue:
	print(f"Unfortunately, there are no more available couriers to deliver the following "
		  f"packages: {', '.join([str(x) for x in packages_stack])}")
elif couriers_queue and not packages_stack:
	print(
		f"Couriers are still on duty: {', '.join([str(x) for x in couriers_queue])} but there are "
		f"no more packages to deliver.")
