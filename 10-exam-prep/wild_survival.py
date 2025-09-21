from collections import deque

bees = deque([int(x) for x in input().split()])
bee_eaters = [int(x) for x in input().split()]

while bees and bee_eaters:
	bee_defender = bees.popleft()
	bee_attacker = bee_eaters.pop()

	if bee_attacker * 7 > bee_defender:
		bee_attacker -= bee_defender // 7
		bee_eaters.append(bee_attacker)

	elif bee_attacker * 7 < bee_defender:
		bee_defender -= bee_attacker * 7
		bees.append(bee_defender)

print("The final battle is over!")
if not bees and not bee_eaters:
	print("But no one made it out alive!")
elif bees:
	print(f"Bee groups left: {', '.join(str(x) for x in bees)}")
elif bee_eaters:
	print(f"Bee-eater groups left: {', '.join(str(x) for x in bee_eaters)}")
