from collections import deque

food_packages = [int(x) for x in input().split()]
food_requests = deque([int(x) for x in input().split()])
target_requests = int(input())

fulfilled_requests = 0

while food_packages and food_requests:
    last_package = food_packages.pop()
    first_request = food_requests.popleft()

    if last_package == first_request:
        fulfilled_requests += 1

    elif last_package > first_request:
        leftover_package = last_package - first_request - 1
        if food_packages and leftover_package > 0:
            food_packages[-1] += leftover_package

        elif not food_packages and leftover_package > 0:
            food_packages.append(leftover_package)

        fulfilled_requests += 1

    else:
        food_requests.append(first_request - last_package)

if fulfilled_requests >= target_requests:
    print(f"Food relief success! Daniel helped {fulfilled_requests} charity points.")

elif 1 <= fulfilled_requests < target_requests:
    print(f"Daniel made a difference! He helped {fulfilled_requests} charity points.")

else:
    print("Daniel could not help much this time. He will try again next week.")

if food_packages:
    print(f"Remaining food packages: {'; '.join(str(x) for x in food_packages[::-1])}")

if food_requests:
    print(f"Unmet food requests: {'; '.join(str(x) for x in food_requests)}")
