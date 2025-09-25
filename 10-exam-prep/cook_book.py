def cookbook(*recipes):
	cuisines_dict = {}
	recipes_dict = {}
	for recipe, cuisine, ingredients in recipes:
		if cuisine not in cuisines_dict:
			cuisines_dict[cuisine] = []
		cuisines_dict[cuisine].append(recipe)
		
		recipes_dict[recipe] = ingredients
	
	for cuisine, recipes in cuisines_dict.items():
		cuisines_dict[cuisine] = sorted(recipes)
	
	sorted_cuisine = sorted(cuisines_dict.items(),
							key=lambda kvp: (-len(kvp[1]), kvp[0]))
	
	output = []
	for cuisine, recipes in sorted_cuisine:
		output.append(f"{cuisine} cuisine contains {len(recipes)} recipes:")
		for recipe in recipes:
			output.append(
				f"  * {recipe} -> Ingredients: "
				f"{', '.join(recipes_dict[recipe])}")
	
	return "\n".join(output)


# print(cookbook(
# 	("Spaghetti Bolognese", "Italian",
# 	 ["spaghetti", "tomato sauce", "ground beef"]),
# 	("Margherita Pizza", "Italian",
# 	 ["pizza dough", "tomato sauce", "mozzarella"]),
# 	("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
# 	("Croissant", "French", ["flour", "butter", "yeast"]),
# 	("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
# ))

# print(cookbook(
# 	("Pad Thai", "Thai",
# 	 ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
# ))

print(cookbook(
	("Spaghetti Bolognese", "Italian",
	 ["spaghetti", "tomato sauce", "ground beef"]),
	("Margherita Pizza", "Italian",
	 ["pizza dough", "tomato sauce", "mozzarella"]),
	("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
	("Croissant", "French", ["flour", "butter", "yeast"]),
	("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
	("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
	("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
	("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
))
