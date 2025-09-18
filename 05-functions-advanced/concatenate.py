def concatenate(*args, **kwargs):
	text = "".join(args)
	for key_part in kwargs.keys():
		if key_part in text:
			text = text.replace(key_part, kwargs[key_part])

	return text

print(concatenate("Soft", "UNI", "Is", "Grate", "!",
				  UNI="Uni", Grate="Great"))

print(concatenate("I", " ", "Love", " ", "Cythons",
				  C="P", s="", java='Java'))
