from collections import deque

robots_data = input().split(";")
robots = []
for robot_params in robots_data:
	robot_name, robot_time = robot_params.split("-")
	robot_time_sec = int(robot_time)
	on_time_to_start = 0
	robots.append({'name': robot_name,
				   'duration': robot_time_sec,
				   'busy until': on_time_to_start})

time_str = input().split(":")
hours, minutes, seconds = map(int, time_str)
start_time_sec = hours * 3600 + minutes * 60 + seconds

products = deque()
prod = input()
while prod != 'End':
	products.append(prod)
	prod = input()

while products:
	curr_product = products.popleft()
	start_time_sec += 1

	for robot in robots:
		if robot['busy until'] <= start_time_sec:
			robot['busy until'] = start_time_sec + robot['duration']
			h = start_time_sec // 3600
			m = (start_time_sec % 3600) // 60
			s = (start_time_sec % 3600) % 60
			h %= 24
			print(f"{robot['name']} - {curr_product} [{h:02d}:{m:02d}:{s:02d}]")
			break
	else:
		products.append(curr_product)
