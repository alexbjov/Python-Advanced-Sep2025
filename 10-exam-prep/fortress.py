from collections import deque

solar_energy_stack = [int(x) for x in input().split(", ")]
distances_queue = deque([int(x) for x in input().split(", ")])

amounts_resources = [
	(80, "Iron"),
	(90, "Titanium"),
	(100, "Aluminium"),
	(60, "Chlorine"),
	(70, "Sulfur")
]

collected_resources = []

while solar_energy_stack and distances_queue:
	last_solar_energy = solar_energy_stack.pop()
	first_distance = distances_queue.popleft()
	
	result = last_solar_energy + first_distance
	if len(amounts_resources) == 0:
		break
	
	if result >= amounts_resources[0][0]:
		collected_resources.append(amounts_resources[0][1])
		amounts_resources.remove(amounts_resources[0])

if len(amounts_resources) == 0:
	print("Mission complete! All minerals have been collected.")
else:
	print("Mission not completed! Awaiting further instructions from Earth.")

if collected_resources:
	output = "Collected resources:\n"
	output += "\n".join(collected_resources)
	print(output)
