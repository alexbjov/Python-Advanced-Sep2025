num_of_users = int(input())
usernames = set()

for _ in range(num_of_users):
	user = input()
	usernames.add(user)

for user in usernames:
	print(user)
