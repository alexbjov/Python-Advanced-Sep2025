def palindrome(word, idx):
	if idx >= len(word) // 2:
		return f"{word} is a palindrome"
	elif word[idx] == word[-idx - 1]:
		return palindrome(word, idx + 1)
	else:
		return f"{word} is not a palindrome"

print(palindrome("abcba", 0))
