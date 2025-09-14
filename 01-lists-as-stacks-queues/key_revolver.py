from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets_stack = list(map(int, input().split()))
locks = deque(map(int, input().split()))
intelligence_value = int(input())

total_money = intelligence_value
start_barrel = barrel_size
while bullets_stack and locks:
	bullet = bullets_stack.pop()
	start_barrel -= 1
	if bullet <= locks[0]:
		locks.popleft()
		print("Bang!")
	else:
		print("Ping!")

	if start_barrel == 0 and bullets_stack:
		print("Reloading!")
		start_barrel = barrel_size

	total_money -= bullet_price

if locks:
	print(f"Couldn't get through. Locks left: {len(locks)}")
else:
	print(f"{len(bullets_stack)} bullets left. Earned ${total_money}")
