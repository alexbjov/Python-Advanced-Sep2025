from collections import deque

money_stack = [int(x) for x in input().split()]
food_queue = deque(int(x) for x in input().split())
num_of_eaten_food = 0

while money_stack and food_queue:
	money = money_stack.pop()
	food = food_queue.popleft()
	
	if money > food:
		money -= food
		if money_stack:
			money_stack[-1] += money
		else:
			money_stack.append(money)
		num_of_eaten_food += 1
	
	elif money == food:
		num_of_eaten_food += 1

if num_of_eaten_food >= 4:
	print(f"Gluttony of the day! Henry ate {num_of_eaten_food} foods.")
elif num_of_eaten_food > 1:
	print(f"Henry ate: {num_of_eaten_food} foods.")
elif num_of_eaten_food == 1:
	print(f"Henry ate: {num_of_eaten_food} food.")
else:
	print("Henry remained hungry. He will try next weekend again.")
