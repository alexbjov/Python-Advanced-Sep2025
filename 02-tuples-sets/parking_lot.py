num_of_cars = int(input())
cars = set()

for _ in range(num_of_cars):
	cmd, car = input().split(', ')
	if cmd == 'IN':
		cars.add(car)
	elif cmd == 'OUT' and car in cars:
		cars.remove(car)

if cars:
	for car in cars:
		print(car)
else:
	print('Parking Lot is Empty')
