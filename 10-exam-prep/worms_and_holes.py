from collections import deque

worms_stack = [int(x) for x in input().split()]
holes_queue = deque([int(x) for x in input().split()])
matches_count = 0
total_worms = len(worms_stack)

while worms_stack and holes_queue:
	last_worm = worms_stack.pop()
	first_hole = holes_queue.popleft()
	
	if last_worm != first_hole:
		last_worm -= 3
		if last_worm > 0:
			worms_stack.append(last_worm)
	
	else:
		matches_count += 1

if matches_count > 0:
	print(f"Matches: {matches_count}")
else:
	print("There are no matches.")

if matches_count == total_worms:
	print("Every worm found a suitable hole!")
else:
	if worms_stack:
		print(f"Worms left: {', '.join([str(worm) for worm in worms_stack])}")
	else:
		print("Worms left: none")

if not holes_queue:
	print("Holes left: none")
else:
	print(f"Holes left: {', '.join([str(hole) for hole in holes_queue])}")
