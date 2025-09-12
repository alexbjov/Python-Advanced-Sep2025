from collections import deque

people_queue = deque()
water_quantity = int(input())

person = input()
while person != "Start":
	people_queue.append(person)
	person = input()

cmd = input()
while cmd != "End":
	if cmd.startswith("refill"):
		water_to_fill = int(cmd.split()[1])
		# print("Added water:", water_to_fill)
		water_quantity += water_to_fill
	elif cmd.isdigit() and people_queue:
		person_left = people_queue.popleft()
		water_to_take = int(cmd)
		if water_to_take <= water_quantity:
			water_quantity -= water_to_take
			print(f"{person_left} got water")
		else:
			print(f"{person_left} must wait")

	cmd = input()

print(f"{water_quantity} liters left")
