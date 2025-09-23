def draw_cards(*monsters, **spells):
	# monster: (card, card_type)
	# spells: card=card_type

	monsters_list = []
	spells_list = []
	for card, card_type in monsters:
		if card_type == 'monster':
			monsters_list.append(card)
		elif card_type == 'spell':
			spells_list.append(card)

	for card, card_type in spells.items():
		if card_type == 'monster':
			monsters_list.append(card)
		elif card_type == 'spell':
			spells_list.append(card)

	output = []
	if monsters_list:
		sorted_monsters = sorted(monsters_list, key=lambda x: x, reverse=True)
		output.append("Monster cards:")
		for card in sorted_monsters:
			output.append(f"  ***{card}")

	if spells_list:
		sorted_spells = sorted(spells_list)
		output.append("Spell cards:")
		for card in sorted_spells:
			output.append(f"  $$${card}")

	return '\n'.join(output)


print(draw_cards(("cyber dragon", "monster"), freeze="spell"))

# print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"),
# 				 raigeki="spell", destroy="spell", ))

# print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell",
# 				 fireball="spell"))
