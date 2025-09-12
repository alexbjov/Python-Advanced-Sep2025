text = input()
letters_stack = []

for i in range(len(text) - 1, -1, -1):
	letters_stack.append(text[i])

print("".join(letters_stack))
