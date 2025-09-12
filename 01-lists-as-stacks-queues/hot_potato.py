from collections import deque

kids_queue = deque(input().split())
n_rotations = int(input()) - 1

while len(kids_queue) > 1:
	kids_queue.rotate(-n_rotations)
	kid_removed = kids_queue.popleft()
	print(f"Removed {kid_removed}")

print(f"Last is {kids_queue[0]}")
