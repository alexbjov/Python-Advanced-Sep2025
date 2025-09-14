from collections import deque

num_of_pumps = int(input())
pumps = deque()

for _ in range(num_of_pumps):
	fuel, distance = map(int, input().split())
	pumps.append((fuel, distance))

start_position = 0
stops = 0

while stops < num_of_pumps:
	tank_fuel = 0
	for current_fuel, current_distance in pumps:
		tank_fuel += current_fuel
		if tank_fuel < current_distance:
			pumps.rotate(-1)
			stops = 0
			start_position += 1
			break

		stops += 1
		tank_fuel -= current_distance

print(start_position)
