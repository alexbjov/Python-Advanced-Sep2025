from math import ceil, floor


def bake_goods(available_trays, *allowed_goods, **customer_orders):
	# goods: (type, trays per batch[int], pieces_per_batch[int)
	# orders: {type, requested_pieces[int]}
	baked_goods = []
	sorted_orders = sorted(customer_orders.items(), key=lambda kvp: kvp[0])
	for requested_good_type, requested_pieces in sorted_orders:
		for available_good_type, trays_per_batch, pieces_per_batch in (
				allowed_goods):
			if requested_good_type == available_good_type:
				needed_batches = ceil(requested_pieces / pieces_per_batch)
				possible_batches = floor(available_trays / trays_per_batch)
				baked_batches = min(needed_batches, possible_batches)
				
				if baked_batches == 0:
					break
				
				produced_pieces = baked_batches * pieces_per_batch
				if produced_pieces > requested_pieces:
					baked_batches = needed_batches
					produced_pieces = requested_pieces
				
				baked_goods.append((requested_good_type, produced_pieces))
				needed_trays = baked_batches * trays_per_batch
				available_trays -= needed_trays
	
	output = []
	if len(baked_goods) == len(allowed_goods) and available_trays > 0:
		output.append(f"All goods baked! Remaining trays: {available_trays}")
	else:
		output.append("Not enough trays!")
	
	output.append("Baked:")
	for good_type, pieces in baked_goods:
		output.append(f"{good_type}: {pieces}")
	
	return "\n".join(output)


print("==================================")
print(bake_goods(9, ("Croissant", 1, 12), ("Bagel", 2, 16), Croissant=24,
				 Bagel=16))
print("==================================")
print(bake_goods(2, ("Muffin", 1, 8), ("Scone", 1, 6), Muffin=12, Scone=6))
print("==================================")
print(bake_goods(3, ("Cookie", 2, 10), ("Donut", 1, 5), Cookie=15, Donut=5))
print("==================================")
print(bake_goods(15, ("Baguette", 1, 4), Croissant=5, Baguette=10, Eclair=1))
print("==================================")
