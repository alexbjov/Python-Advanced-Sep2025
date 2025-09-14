from collections import deque

cups_queue = deque(map(int, input().split()))
bottles_stack = list(map(int, input().split()))
wasted_water = 0

while cups_queue and bottles_stack:
	current_cup = cups_queue[0]
	current_bottle = bottles_stack[-1]

	if current_bottle >= current_cup:
		current_bottle -= current_cup
		cups_queue.popleft()
		bottles_stack.pop()
		wasted_water += current_bottle
	else:
		while current_cup > 0:
			current_cup -= current_bottle
			if bottles_stack:
				bottles_stack.pop()
				current_bottle = bottles_stack[-1]
				if current_bottle >= current_cup:
					wasted_water += current_bottle - current_cup
					bottles_stack.pop()
					cups_queue.popleft()
					break

if cups_queue:
	print("Cups:", *cups_queue)
elif bottles_stack:
	print("Bottles:", *reversed(bottles_stack))

print(f"Wasted litters of water: {wasted_water}")
