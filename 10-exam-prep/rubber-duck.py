from collections import deque

time_for_tasks = deque(int(x) for x in input().split())
num_of_tasks = [int(x) for x in input().split()]

time_duck = {
    60: "Darth Vader Ducky",
    120: "Thor Ducky",
    180: "Big Blue Rubber Ducky",
    240: "Small Yellow Rubber Ducky"
}

max_value = 240
duck_count = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0
}

while time_for_tasks and num_of_tasks:
    first_time = time_for_tasks[0]
    last_num = num_of_tasks[-1]
    
    result = first_time * last_num
    if result > max_value:
        num_of_tasks[-1] -= 2
        time_for_tasks.rotate(-1)
    else:
        for duck_time, duck_type in time_duck.items():
            if result <= duck_time:
                duck_count[duck_type] += 1
                break
        
        time_for_tasks.popleft()
        num_of_tasks.pop()

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
output = [
    f"Darth Vader Ducky: {duck_count['Darth Vader Ducky']}",
    f"Thor Ducky: {duck_count['Thor Ducky']}",
    f"Big Blue Rubber Ducky: {duck_count['Big Blue Rubber Ducky']}",
    f"Small Yellow Rubber Ducky: {duck_count['Small Yellow Rubber Ducky']}"
]
print("\n".join(output))
