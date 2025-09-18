def age_assignment(*args, **kwargs):
	data = {}
	for first_letter, age in kwargs.items():
		for name in args:
			if first_letter == name[0]:
				data[name] = kwargs[first_letter]
				break

	result_data = sorted(data.items(), key=lambda kvp: kvp[0])
	text = ""
	for name, age in result_data:
		text += f"{name} is {age} years old.\n"
	return text

print(age_assignment(
	"Peter", "George",
	G=26, P=19)
)

print(age_assignment(
	"Amy", "Bill", "Willy",
	W=36, A=22, B=61)
)
