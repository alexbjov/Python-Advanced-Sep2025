from collections import deque

tools_queue = deque(map(int, input().split()))
substances_stack = list(map(int, input().split()))
challenges = [int(x) for x in input().split()]

while tools_queue and substances_stack:
	first_tool = tools_queue.popleft()
	last_substance = substances_stack.pop()
	product = first_tool * last_substance
	
	if product in challenges:
		challenges.remove(product)
	else:
		tools_queue.append(first_tool + 1)
		last_substance -= 1
		if last_substance > 0:
			substances_stack.append(last_substance)

if challenges:
	print("Harry is lost in the temple. Oblivion awaits him.")
else:
	print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools_queue:
	print(f"Tools: {', '.join(str(x) for x in tools_queue)}")

if substances_stack:
	print(f"Substances: {', '.join(str(x) for x in substances_stack)}")

if challenges:
	print(f"Challenges: {', '.join(str(x) for x in challenges)}")
