def accommodate_new_pets(hotel_capacity: int, max_weight: float,
		*pets_weight) -> str:
	pet_types: dict[str, list[float]] = {}
	num_of_pets: int = 0
	all_accommodated: bool = True
	
	for pet, weight in pets_weight:
		if num_of_pets == hotel_capacity:
			all_accommodated = False
			break
		
		if weight > max_weight:
			continue
		
		if pet not in pet_types:
			pet_types[pet] = []
		pet_types[pet].append(weight)
		num_of_pets += 1
	
	result = []
	if all_accommodated:
		result.append(
			f"All pets are accommodated! Available capacity: {hotel_capacity - num_of_pets}.")
	
	else:
		result.append("You did not manage to accommodate all pets!")
	
	result.append("Accommodated pets:")
	if pet_types:
		sorted_pet_types = sorted(pet_types.items(), key=lambda kvp: kvp[0])
		for pet, weight_list in sorted_pet_types:
			result.append(f"{pet}: {len(weight_list)}")
	
	return "\n".join(result)


print(accommodate_new_pets(10, 15.0, ("cat", 5.8), ("dog", 10.0), ))

# print(
# 	accommodate_new_pets(10, 10.0, ("cat", 5.8), ("dog", 10.5), ("parrot", 0.8),
# 		("cat", 3.1), ))

# print(
# 	accommodate_new_pets(2, 15.0, ("dog", 10.0), ("cat", 5.8), ("cat", 2.7), ))
