from collections import deque

people_queue = deque()

customer = input()
while customer != "End":
	if customer == "Paid":
		while people_queue:
			customer_paid = people_queue.popleft()
			print(customer_paid)
	else:
		people_queue.append(customer)
	customer = input()

print(f"{len(people_queue)} people remaining.")
