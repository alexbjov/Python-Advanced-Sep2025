from collections import deque

robots_data = input().split(";")
start_time = input().split(":")
hours, minutes, seconds = map(int, start_time)
total_time_sec = hours * 3600 + minutes * 60 + seconds
added_time = 1
product_time = total_time_sec + added_time

robots = deque()
for robot_params in robots_data:
	robot_name, robot_time = robot_params.split("-")
	robot_time_sec = int(robot_time)
	on_time_to_start = product_time
	robots.append([robot_name, robot_time_sec, on_time_to_start])

products = deque()
product = input()
# to be continued
# while product != "End":
# 	products.append(product)
# 	current_robot = robots.popleft()
# 	while product_time < current_robot[2]:
# 		robots.append(current_robot)
# 		current_robot = robots.popleft()
# 	if product_time >= current_robot[2]:
# 		print(f"{current_robot[0]} - {product} {product_time}")
# 		current_robot[2] = product_time + current_robot[1]
# 		robots.append(current_robot)
# 		products.popleft()
#
#
# 	product_time += added_time
# 	product = input()
