from collections import deque

greenlight_duration = int(input())
free_window_to_pass = int(input())

command = input()
start_time = 0
safe_cars_counter = 0
cars = deque()
crashed_car = False
car_model = ""

while command != 'End':
	current_car_model = command
	if command != 'green':
		cars.append(current_car_model)
		continue

	car_model = cars.popleft()
	if len(car_model) <= greenlight_duration:
		safe_cars_counter += 1
	else:
		crashed_car = True
		break

	command = input()

if crashed_car:
	print("A crash happened!")
	print(f"{car_model} was hit at {5}.")
else:
	print("Everyone is safe.")
	print(f"{safe_cars_counter} total cars passed the crossroads.")
