n, m = [int(x) for x in input().split()]

set1 = set()
set2 = set()

for _ in range(n):
	num = int(input())
	set1.add(num)

for _ in range(m):
	num = int(input())
	set2.add(num)

common_elements = set1 & set2

for elem in common_elements:
	print(elem)
