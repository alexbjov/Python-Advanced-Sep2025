from collections import deque

bees_queue = deque([int(x) for x in input().split()])
nectar_stack = [int(x) for x in input().split()]
symbols = deque(input().split())
operators = {
	'+': lambda x, y: x + y,
	'-': lambda x, y: x - y,
	'*': lambda x, y: x * y,
	'/': lambda x, y: x / y if y != 0 else 0
}

sum_honey = 0

while bees_queue and nectar_stack:
	current_bee = bees_queue[0]
	current_nectar = nectar_stack[-1]

	if current_nectar >= current_bee:
		sum_honey += abs(operators[symbols[0]](current_bee, current_nectar))
		nectar_stack.pop()
		bees_queue.popleft()
		symbols.popleft()
	else:
		nectar_stack.pop()

print(f'Total honey made: {sum_honey}')
if bees_queue:
	print(f'Bees left: {", ".join(str(x) for x in bees_queue)}')
if nectar_stack:
	print(f'Nectar left: {", ".join(str(x) for x in nectar_stack)}')
