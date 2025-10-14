def team_lineup(*players_countries):
	countries = {}
	for player, country in players_countries:
		if country not in countries:
			countries[country] = []
		countries[country].append(player)
	
	sorted_countries = sorted(countries.items(),
		key=lambda kvp: (-len(kvp[1]), kvp[0]))
	
	result = []
	for country, players in sorted_countries:
		result.append(f"{country}:")
		for player in players:
			result.append(f"  -{player}")
	
	return "\n".join(result)


# print(team_lineup(("Harry Kane", "England"), ("Manuel Neuer", "Germany"),
# 	("Raheem Sterling", "England"), ("Toni Kroos", "Germany"),
# 	("Cristiano Ronaldo", "Portugal"), ("Thomas Muller", "Germany")))

# print(team_lineup(("Lionel Messi", "Argentina"), ("Neymar", "Brazil"),
# 	("Cristiano Ronaldo", "Portugal"), ("Harry Kane", "England"),
# 	("Kylian Mbappe", "France"), ("Raheem Sterling", "England")))

print(team_lineup(("Harry Kane", "England"), ("Manuel Neuer", "Germany"),
	("Raheem Sterling", "England"), ("Toni Kroos", "Germany"),
	("Cristiano Ronaldo", "Portugal"), ("Thomas Muller", "Germany"),
	("Bruno Fernandes", "Portugal"), ("Bernardo Silva", "Portugal"),
	("Harry Maguire", "England")))
