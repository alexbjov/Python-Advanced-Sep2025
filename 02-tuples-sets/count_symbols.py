text = input()

symbols = {}

for character in text:
	if character not in symbols:
		symbols[character] = text.count(character)

sorted_symbols = sorted(symbols)

for character in sorted_symbols:
	print(f"{character}: {symbols[character]} time/s")
