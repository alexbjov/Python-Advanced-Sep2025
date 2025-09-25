from collections import deque

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

presents = {
	150: "Doll",
	250: "Wooden train",
	300: "Teddy bear",
	400: "Bicycle"
}

crafted_toys = []

while materials and magic:
	if materials[-1] == 0 or magic[0] == 0:
		
		if materials[-1] == 0:
			materials.pop()
		
		if magic[0] == 0:
			magic.popleft()
		
		continue
	
	last_material = materials.pop()
	first_magic = magic.popleft()
	
	total_magic = last_material * first_magic
	if total_magic in presents:
		new_present = presents[total_magic]
		crafted_toys.append(new_present)
	
	elif total_magic < 0:
		materials.append(last_material + first_magic)
	
	elif total_magic > 0:
		materials.append(last_material + 15)

if (({'Doll', "Wooden train"}.issubset(crafted_toys)) or
		({'Teddy bear', 'Bicycle'}.issubset(crafted_toys))):
	print('The presents are crafted! Merry Christmas!')
else:
	print("No presents this Christmas!")

if materials:
	print(f"Materials left: {', '.join([str(x) for x in materials[::-1]])}")

if magic:
	print(f"Magic left: {', '.join([str(x) for x in magic])}")

unique_toys = sorted(list(set(crafted_toys)))

for toy in unique_toys:
	print(f"{toy}: {crafted_toys.count(toy)}")
