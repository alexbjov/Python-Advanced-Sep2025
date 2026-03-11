from collections import deque

caffeine_stack = [int(x) for x in input().split(", ")]
drinks_queue = deque([int(x) for x in input().split(", ")])

total_caffeine = 300
initial_caffeine = 0

while caffeine_stack and drinks_queue:
    last_caffeine = caffeine_stack.pop()
    first_drink = drinks_queue[0]

    calculated_caffeine = last_caffeine * first_drink
    if initial_caffeine + calculated_caffeine <= total_caffeine:
        drinks_queue.popleft()
        initial_caffeine += calculated_caffeine

    else:
        drinks_queue.rotate(-1)
        initial_caffeine -= 30

        if initial_caffeine < 0:
            initial_caffeine = 0

if drinks_queue:
    print(f"Drinks left: {', '.join(str(x) for x in drinks_queue)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {initial_caffeine} mg caffeine.")
