from collections import deque

strength = [int(x) for x in input().split()]
accuracy = deque(int(x) for x in input().split())

total_scored_goals = 0
target = 100

while strength and accuracy:
	last_strength = strength.pop()
	first_accuracy = accuracy.popleft()

	current_sum = last_strength + first_accuracy
	if current_sum == target:
		total_scored_goals += 1

	elif current_sum < target:
		if last_strength < first_accuracy:
			accuracy.appendleft(first_accuracy)
		elif last_strength > first_accuracy:
			strength.append(last_strength)
		else:
			strength.append(current_sum)

	else:
		last_strength -= 10
		strength.append(last_strength)
		accuracy.append(first_accuracy)

if total_scored_goals == 3:
	print("Paul scored a hat-trick!")
elif total_scored_goals == 0:
	print("Paul failed to score a single goal.")
elif total_scored_goals > 3:
	print("Paul performed remarkably well!")
elif 0 < total_scored_goals < 3:
	print("Paul failed to make a hat-trick.")

if total_scored_goals > 0:
	print(f"Goals scored: {total_scored_goals}")

if strength:
	print(f"Strength values left: {', '.join([str(x) for x in strength])}")
if accuracy:
	print(f"Accuracy values left: {', '.join([str(x) for x in accuracy])}")
