def calc_factorial(n: int) -> int:
	if n == 1:
		return 1
	
	return n * calc_factorial(n - 1)


num = int(input())
result = calc_factorial(num)
print(result)
