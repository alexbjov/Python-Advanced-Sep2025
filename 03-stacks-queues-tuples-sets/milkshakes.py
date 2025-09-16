from collections import deque

chocolate_stack = [int(x) for x in input().split(', ')]
milk_deque = deque([int(x) for x in input().split(', ')])

num_of_milkshakes = 0

while chocolate_stack and milk_deque and num_of_milkshakes < 5:
	last_chocolate = chocolate_stack[-1]
	first_milk = milk_deque[0]

	if last_chocolate <= 0 and first_milk <= 0:
		chocolate_stack.pop()
		milk_deque.popleft()
		continue

	if last_chocolate <= 0:
		chocolate_stack.pop()
		continue

	if first_milk <= 0:
		milk_deque.popleft()
		continue

	if last_chocolate == first_milk:
		chocolate_stack.pop()
		milk_deque.popleft()
		num_of_milkshakes += 1
	else:
		milk_deque.rotate(-1)
		chocolate_stack[-1] -= 5

if num_of_milkshakes == 5:
	print('Great! You made all the chocolate milkshakes needed!')
else:
	print('Not enough milkshakes.')

if chocolate_stack:
	print(f'Chocolate: {", ".join(str(x) for x in chocolate_stack)}')
else:
	print('Chocolate: empty')

if milk_deque:
	print(f'Milk: {", ".join(str(x) for x in milk_deque)}')
else:
	print('Milk: empty')
