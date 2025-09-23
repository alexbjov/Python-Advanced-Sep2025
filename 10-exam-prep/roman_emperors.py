def list_roman_emperors(*emperors_success, **emperors_length):
	successful_emperors = {}
	unsuccessful_emperors = {}
	for emperor, success in emperors_success:
		if success:
			successful_emperors[emperor] = emperors_length[emperor]
		else:
			unsuccessful_emperors[emperor] = emperors_length[emperor]

	sorted_successful_emperors = sorted(successful_emperors.items(),
										key=lambda kvp: (-kvp[1], kvp[0]))

	sorted_unsuccessful_emperors = sorted(unsuccessful_emperors.items(),
										  key=lambda kvp: (kvp[1], kvp[0]))

	output = [f"Total number of emperors: {len(emperors_length)}"]
	if successful_emperors:
		output.append("Successful emperors:")
		for emperor, rule in sorted_successful_emperors:
			output.append(f"****{emperor}: {rule}")
	if unsuccessful_emperors:
		output.append("Unsuccessful emperors:")
		for emperor, rule in sorted_unsuccessful_emperors:
			output.append(f"****{emperor}: {rule}")

	return '\n'.join(output)


# print(list_roman_emperors(("Augustus", True), ("Nero", False), Augustus=40, Nero=14, ))

# print(
# 	list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False), ("Caligula", False),
# 						("Pertinax", False), ("Vespasian", True), Augustus=40, Trajan=19, Nero=14,
# 						Caligula=4, Pertinax=4, Vespasian=19, ))

print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Claudius", True), Augustus=40,
						  Trajan=19, Claudius=13, ))
