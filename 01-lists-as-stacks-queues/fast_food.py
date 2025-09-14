from collections import deque

total_food = int(input())
orders = deque(int(order) for order in input().split())

print(max(orders))
while orders and orders[0] <= total_food:
	total_food -= orders.popleft()

if orders:
	print("Orders left:", *orders)
else:
	print("Orders complete")
