import math


def plant_garden(garden_capacity: int, *plants_info, **requested_plants_info):
	max_plants = sum(requested_plants_info.values())
	free_space = garden_capacity
	num_of_planted = 0
	sorted_requested = sorted(requested_plants_info.items(), key=lambda kvp: kvp[0])
	planted_garden = {}
	num_of_not_planted = 0
	messages = []
	for plant, quantity in sorted_requested:
		if plant not in planted_garden:
			planted_garden[plant] = 0
		for plant_details in plants_info:
			if plant == plant_details[0]:

				if free_space // plant_details[1] >= quantity:
					num_of_planted += quantity
					free_space -= plant_details[1] * quantity
					planted_garden[plant] += quantity

				else:
					new_quantity = math.floor(free_space // plant_details[1])
					num_of_planted += new_quantity
					free_space -= plant_details[1] * new_quantity
					if new_quantity != 0:
						planted_garden[plant] += new_quantity

	if max_plants <= garden_capacity:
		print(f"All plants were planted! Available garden space: {free_space:.1f} sq meters.")
	else:
		messages.append("Not enough space to plant all requested plants!")
	messages.append("Planted plants:")
	for plant, num in planted_garden.items():
		if num > 0:
			messages.append(f"{plant}: {num}")
	return '\n'.join(messages)


# print(plant_garden(50.0, ("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20))

# print(plant_garden(20.0, ("rose", 2.0), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20,
# 				   sunflower=5))

# print(
# 	plant_garden(2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2), rose=4, tulip=15, sunflower=3,
# 				 daisy=4))

print(plant_garden(50.0, ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, daisy=1))
