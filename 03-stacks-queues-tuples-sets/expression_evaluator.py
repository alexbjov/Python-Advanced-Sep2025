from collections import deque

expression = input().split()
numbers = deque()

for character in expression:
	if character not in '+-*/':
		numbers.append(int(character))
	else:
		while len(numbers) > 1:
			first_num = numbers.popleft()
			second_num = numbers.popleft()
			if character == '+':
				numbers.appendleft(first_num + second_num)
			elif character == '-':
				numbers.appendleft(first_num - second_num)
			elif character == '*':
				numbers.appendleft(first_num * second_num)
			elif character == '/':
				numbers.appendleft(first_num // second_num)

print(numbers[0])
