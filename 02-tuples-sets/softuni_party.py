num_of_guests = int(input())
reservations = set()

for _ in range(num_of_guests):
	guest = input()
	reservations.add(guest)

guest_to_remove = input()

while guest_to_remove != 'END':
	if guest_to_remove in reservations:
		reservations.remove(guest_to_remove)
	guest_to_remove = input()

print(len(reservations))
sorted_reservations = sorted(reservations)

for guest in sorted_reservations:
	print(guest)
