def calc_coins(coins: list[int], target: int):
	coins.sort(reverse=True)
	used_coins = {}
	
	idx = 0
	while target > 0 and idx < len(coins):
		count_coins = target // coins[idx]
		target %= coins[idx]
		
		if count_coins > 0:
			used_coins[coins[idx]] = count_coins
		
		idx += 1
	
	if target > 0:
		return "Error"
	
	result = [f"Number of coins to take: {sum(used_coins.values())}"]
	for val, count in used_coins.items():
		result.append(f"{count} coin(s) with value {val}")
	
	return "\n".join(result)


coins_list: list[int] = [int(x) for x in input().split(", ")]
target_sum = int(input())

print(calc_coins(coins_list, target_sum))
