rows = int(input())

matrix = [[int(el) for el in input().split(', ') if int(el) % 2 == 0]
		  for _ in range(rows)]

# matrix = []
# for _ in range(rows):
# 	row_data = [int(el) for el in input().split(', ') if int(el) % 2 == 0]
# 	matrix.append(row_data)

print(matrix)
