from collections import deque

potions: dict[int, str] = {110: "Brew of Immortality",
						   100: "Essence of Resilience",
						   90: "Draught of Wisdom", 80: "Potion of Agility",
						   70: "Elixir of Strength"}

crafted_potions: list[str] = []
substances = [int(x) for x in input().split(', ')]
crystals = deque(int(x) for x in input().split(', '))

while potions and substances and crystals:
	last_substance = substances.pop()
	first_crystal = crystals.popleft()
	
	total_energy = last_substance + first_crystal
	if total_energy in potions:
		crafted_potions.append(potions[total_energy])
		del potions[total_energy]
	else:
		for energy, potion in potions.items():
			if total_energy > energy:
				crafted_potions.append(potions[energy])
				del potions[energy]
				first_crystal -= 20
				if first_crystal > 0:
					crystals.append(first_crystal)
				break
		
		else:
			first_crystal -= 5
			if first_crystal > 0:
				crystals.append(first_crystal)

if potions:
	print("The alchemist failed to complete his quest.")
else:
	print("Success! The alchemist has forged all potions!")

if crafted_potions:
	print(f"Crafted potions: {', '.join(str(x) for x in crafted_potions)}")

if substances:
	print(f"Substances: {', '.join(str(x) for x in reversed(substances))}")

if crystals:
	print(f"Crystals: {', '.join(str(x) for x in crystals)}")
