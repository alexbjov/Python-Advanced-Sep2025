def boarding_passengers(ship_capacity, *passenger_groups):
	available_ship_seats = ship_capacity
	passengers_details = {}
	total_passengers = sum(x[0] for x in passenger_groups)

	for num_of_passengers, category in passenger_groups:
		if num_of_passengers <= available_ship_seats:
			if category not in passengers_details:
				passengers_details[category] = 0
			passengers_details[category] += num_of_passengers
			available_ship_seats -= num_of_passengers

		if available_ship_seats == 0:
			break

	sorted_list = sorted(passengers_details.items(), key=lambda kvp: (-kvp[1], kvp[0]))
	result = [f"Boarding details by benefit plan:"]
	for program, num_of_guests in sorted_list:
		result.append(f"## {program}: {num_of_guests} guests")

	if total_passengers <= ship_capacity:
		result.append("All passengers are successfully boarded!")
	elif available_ship_seats == 0:
		result.append("Boarding unsuccessful. Cruise ship at full capacity.")
	else:
		result.append(
			f"Partial boarding completed. Available capacity: {available_ship_seats}.")
	return "\n".join(result)


# print(boarding_passengers(150,
# 						  (35, 'Diamond'),
# 						  (55, 'Platinum'),
# 						  (35, 'Gold'),
# 						  (25, 'First Cruiser'))
# 	  )

print(
	boarding_passengers(100,
						(20, 'Diamond'),
						(15, 'Platinum'),
						(25, 'Gold'),
						(25, 'First Cruiser'),
						(15, 'Diamond'),
						(10, 'Gold'))
)

# print(
# 	boarding_passengers(120,
# 						(30, 'Gold'),
# 						(20, 'Platinum'),
# 						(30, 'Diamond'),
# 						(10, 'First Cruiser'),
# 						(31, 'Platinum'),
# 						(20, 'Diamond'))
# )
