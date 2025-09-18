def func_executor(*args):
	text = ""
	for items in args:
		func = items[0]
		func_args = items[1]
		result = func(*func_args)
		text += f"{func.__name__} - {result}\n"

	return text

def sum_numbers(num1, num2):
	return num1 + num2

def multiply_numbers(num1, num2):
	return num1 * num2

print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
