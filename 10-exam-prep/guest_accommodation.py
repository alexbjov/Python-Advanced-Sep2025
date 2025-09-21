def accommodate(*args, **kwargs):
	available_rooms = {}
	unaccommodated_guests = 0
	for room, num_as_str in kwargs.items():
		room_number = int(room.split('_')[1])
		capacity = int(num_as_str)
		available_rooms[room_number] = capacity

	sorted_rooms = sorted(available_rooms.items(), key=lambda kvp: (kvp[1], kvp[0]))

	occupied_rooms = {}
	for guest_num in args:
		for room_num, capacity in sorted_rooms:
			if guest_num <= capacity:
				occupied_rooms[room_num] = guest_num
				sorted_rooms.remove((room_num, capacity))
				break

		else:
			unaccommodated_guests += guest_num

	result = []
	if occupied_rooms:
		sorted_occupied_rooms = sorted(occupied_rooms.items(), key=lambda kvp: kvp[0])
		result.append(f"A total of {len(occupied_rooms)} accommodations were completed!")
		for room, guests in sorted_occupied_rooms:
			result.append(f"<Room {room} accommodates {guests} guests>")

	else:
		result.append("No accommodations were completed!")

	if unaccommodated_guests > 0:
		result.append(f"Guests with no accommodation: {unaccommodated_guests}")

	empty_rooms = len(available_rooms) - len(occupied_rooms)
	if empty_rooms > 0:
		result.append(f"Empty rooms: {empty_rooms}")

	return '\n'.join(result)


print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))

# print(accommodate(10, 9, 8, room_307=6, room_802=5))

# print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))
