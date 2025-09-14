expression = input()
stack = []

parentheses = {
	"(": ")",
	"[": "]",
	"{": "}"
}

for character in expression:
	if character in parentheses:
		stack.append(character)
	else:
		if not stack:
			print("NO")
			break
		last_opening_parenthesis = stack.pop()
		if parentheses[last_opening_parenthesis] != character:
			print("NO")
			break

else:
	if stack:
		print("NO")
	else:
		print("YES")
