from collections import deque

suggested_links = deque(int(x) for x in input().split())
featured_links = [int(x) for x in input().split()]

final_feed = []

total_engagement_value = 0
target = int(input())

while suggested_links and featured_links:
	engagement_score = suggested_links.popleft()
	popularity_score = featured_links.pop()

	if engagement_score < popularity_score:
		el = popularity_score % engagement_score
		final_feed.append(el)
		el *= 2
		if el != 0:
			featured_links.append(el)

	elif engagement_score > popularity_score:
		el = engagement_score % popularity_score
		final_feed.append(-el)
		el *= 2
		if el != 0:
			suggested_links.append(el)

	else:
		final_feed.append(0)

total_engagement_value = sum(final_feed)
print(f"Final Feed: {', '.join([str(x) for x in final_feed])}")

if total_engagement_value >= target:
	print(f"Goal achieved! Engagement Value: {total_engagement_value}")
else:
	print(f"Goal not achieved! Short by: {target - total_engagement_value}")
