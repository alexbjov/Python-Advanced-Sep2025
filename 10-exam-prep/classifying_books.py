def classify_books(*genre_title, **isbn_title):
	fiction_books = {}
	non_fiction_books = {}
	
	for isbn, title in isbn_title.items():
		for genre, book_title in genre_title:
			if title == book_title and genre == "fiction":
				fiction_books[isbn] = title
				break
			
			elif title == book_title and genre == "non_fiction":
				non_fiction_books[isbn] = title
				break
	
	sorted_fiction = sorted(fiction_books.items(), key=lambda kvp: kvp[0])
	sorted_non_fiction = sorted(non_fiction_books.items(),
		key=lambda kvp: kvp[0], reverse=True)
	
	result = []
	if fiction_books:
		result.append("Fiction Books:")
		for isbn, title in sorted_fiction:
			result.append(f"~~~{isbn}#{title}")
	
	if non_fiction_books:
		result.append("Non-Fiction Books:")
		for isbn, title in sorted_non_fiction:
			result.append(f"***{isbn}#{title}")
	
	return "\n".join(result)


# print(classify_books(("fiction", "Brave New World"),
# 	("non_fiction", "The Art of War"), NF3421NN="The Art of War",
# 	FF1234UU="Brave New World"))

# print(classify_books(("non_fiction", "The Art of War"),
# 	("fiction", "The Great Gatsby"), ("non_fiction", "A Brief History of Time"),
# 	("fiction", "Brave New World"), FF1234HH="The Great Gatsby",
# 	NF3845UU="A Brief History of Time", NF3421NN="The Art of War",
# 	FF1234UU="Brave New World"))

# print(classify_books(("fiction", "Brave New World"),
# 	("fiction", "The Catcher in the Rye"), ("fiction", "1984"),
# 	FICCITRZZ="The Catcher in the Rye", FIC1984XX="1984",
# 	FICBNWYYY="Brave New World"))

print(classify_books(("non_fiction", "Sapiens"), ("non_fiction", "Homo Deus"),
	("non_fiction", "The Selfish Gene"), NF123ABC="Sapiens",
	NF987XYZ="Homo Deus", NF456DEF="The Selfish Gene"))
