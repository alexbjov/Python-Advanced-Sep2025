from _collections import deque

fuel_stack = list(map(int, input().split()))
consumption_queue = deque(list(map(int, input().split())))
needed_fuel_queue = deque(int(x) for x in input().split())

total = len(fuel_stack)
reached_alt = []
count = 1
while fuel_stack and consumption_queue:
	last_fuel = fuel_stack[-1]
	first_consumption = consumption_queue[0]
	
	difference = last_fuel - first_consumption
	if difference >= needed_fuel_queue[0]:
		fuel_stack.pop()
		consumption_queue.popleft()
		needed_fuel_queue.popleft()
		print(f"John has reached: Altitude {count}")
		reached_alt.append(f"Altitude {count}")
	
	else:
		print(f"John did not reach: Altitude {count}")
		break
	
	count += 1

if fuel_stack and count > 1:
	print("John failed to reach the top.")
	print(f"Reached altitudes: {', '.join(reached_alt)}")

elif fuel_stack and count == 1:
	print("John failed to reach the top.")
	print("John didn't reach any altitude.")

elif total == count - 1:
	print("John has reached all the altitudes and managed to reach the top!")
