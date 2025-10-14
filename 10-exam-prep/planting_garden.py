import math


def plant_garden(garden_space: float, *allowed_plants_space,
		**requested_plants_pieces) -> str:
	sorted_requests = sorted(requested_plants_pieces.items(),
		key=lambda x: x[0])
	
	plants_list = []
	result = []
	out_of_space = False
	
	for plant, pieces in sorted_requests:
		for allowed_plant, space in allowed_plants_space:
			if plant == allowed_plant:
				needed_plant_space = min(pieces * space, garden_space)
				needed_pieces = math.floor(needed_plant_space / space)
				if needed_pieces > 0:
					plants_list.append((plant, needed_pieces))
					garden_space -= needed_plant_space
				break
		
		if garden_space <= 0.0:
			out_of_space = True
			break
	
	total_planted = sum(item[1] for item in plants_list)
	total_requested = sum(item[1] for item in sorted_requests)
	# print("Total planted:", total_planted)
	# print("Total requested:", total_requested)
	
	if total_planted == total_requested or not out_of_space:
		result.append(
			f"All plants were planted! Available garden space: {garden_space:.1f} sq meters.")
	
	else:
		result.append("Not enough space to plant all requested plants!")
	
	result.append("Planted plants:")
	for plant, pieces in plants_list:
		result.append(f"{plant}: {pieces}")
	
	return "\n".join(result)


print(plant_garden(50.0, ("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0),
	rose=10, tulip=20))

# print(plant_garden(20.0, ("rose", 2.0), ("tulip", 1.2), ("sunflower", 3.0),
# 	rose=10, tulip=20, sunflower=5))

# print(plant_garden(2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2), rose=4,
# 	tulip=15, sunflower=3, daisy=4))

# print(plant_garden(50.0, ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20,
# 	daisy=1))
