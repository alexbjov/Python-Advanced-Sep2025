expression = input()
parenthesis_stack = []

for i in range(len(expression)):
	if expression[i] == "(":
		parenthesis_stack.append(i)
	elif parenthesis_stack and expression[i] == ")":
		start_idx = parenthesis_stack.pop()
		end_idx = i + 1
		print(expression[start_idx:end_idx])
