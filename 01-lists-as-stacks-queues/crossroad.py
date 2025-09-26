from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())
crossroad = deque()
crash = False
total_cars = 0
hit_index = -1
car = ""

command = input()
while command != 'END':
	if command != 'green':
		crossroad.append(command)
	else:
		time = green_light_duration
		
		while crossroad and time > 0:
			car = crossroad.popleft()
			car_length = len(car)
			
			if car_length <= time:
				time -= car_length
				total_cars += 1
			
			elif car_length <= time + free_window_duration:
				total_cars += 1
				time = 0
			
			else:
				hit_index = time + free_window_duration
				if hit_index >= len(car):
					hit_index = len(car) - 1
				
				crash = True
				break
		
		if crash:
			break
	
	command = input()

if crash:
	print("A crash happened!")
	print(f"{car} was hit at {car[hit_index]}.")
else:
	print("Everyone is safe.")
	print(f"{total_cars} total cars passed the crossroads.")
