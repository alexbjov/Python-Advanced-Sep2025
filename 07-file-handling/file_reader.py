import os

path = os.path.join("lab_files", "numbers.txt")
file = open(path)

nums = [int(el) for el in file.read().split('\n') if el]
print(sum(nums))
file.close()
