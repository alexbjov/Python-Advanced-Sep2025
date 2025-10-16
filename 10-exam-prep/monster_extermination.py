from _collections import deque

monsters_armor_queue = deque(map(int, input().split(',')))
soldier_strikes = list(map(int, input().split(',')))
monsters_killed = 0
while monsters_armor_queue and soldier_strikes:
	first_armor = monsters_armor_queue.popleft()
	last_strike = soldier_strikes.pop()
	
	if last_strike > first_armor:
		monsters_killed += 1
		difference = last_strike - first_armor
		if soldier_strikes:
			soldier_strikes[-1] += difference
		else:
			soldier_strikes.append(difference)
	
	elif last_strike < first_armor:
		difference = first_armor - last_strike
		monsters_armor_queue.append(difference)
	
	else:
		monsters_killed += 1

if not monsters_armor_queue:
	print("All monsters have been killed!")

if not soldier_strikes:
	print("The soldier has been defeated.")

print(f"Total monsters killed: {monsters_killed}")
