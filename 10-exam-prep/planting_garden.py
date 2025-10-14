def plant_garden(garden_space: float, *allowed_plants_space,
		**requested_plants_pieces) -> str:
	sorted_requests = sorted(requested_plants_pieces.items(),
		key=lambda x: x[0])
	
	plants_list = []
	all_planted = True
	
	for plant, pieces in sorted_requests:
		for allowed_plant, space in allowed_plants_space:
			if plant == allowed_plant:
				planted = min(pieces, int(garden_space / space))
				if planted < pieces:
					all_planted = False
				
				if planted > 0:
					plants_list.append((plant, planted))
					garden_space -= planted * space
				
				break
	
	result = []
	if all_planted:
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
