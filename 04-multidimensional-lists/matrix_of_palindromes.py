rows, cols = map(int, input().split())
start = ord('a')
matrix = []

for i in range(rows):
	row_data = [""] * cols
	next_num = start
	for j in range(cols):
		palindrome = f"{chr(start)}{chr(next_num)}{chr(start)}"
		row_data[j] = palindrome
		next_num += 1
	matrix.append(row_data)
	start += 1

for i in range(rows):
	print(*matrix[i])
