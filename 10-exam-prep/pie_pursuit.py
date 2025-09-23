from collections import deque

contestants = deque([int(x) for x in input().split()])
pies = [int(x) for x in input().split()]

while contestants and pies:
	first_contestant = contestants.popleft()
	last_pie = pies.pop()

	if first_contestant >= last_pie:
		first_contestant -= last_pie
		if first_contestant > 0:
			contestants.append(first_contestant)

	else:
		last_pie -= first_contestant
		if last_pie > 1:
			pies.append(last_pie)
		elif last_pie == 1 and pies:
			pies[-1] += 1
		elif last_pie == 1 and not pies:
			pies = [last_pie]

if not contestants and not pies:
	print("We have a champion!")

elif contestants:
	print("We will have to wait for more pies to be baked!")
	print(f"Contestants left: {', '.join([str(x) for x in contestants])}")

elif pies:
	print("Our contestants need to rest!")
	print(f"Pies left: {', '.join([str(x) for x in pies])}")
