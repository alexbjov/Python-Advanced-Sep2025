def even_odd_filter(**kwargs):
	if 'odd' in kwargs:
		kwargs['odd'] = [el for el in kwargs['odd'] if el % 2 != 0]
	if 'even' in kwargs:
		kwargs['even'] = [el for el in kwargs['even'] if el % 2 == 0]

	sorted_lst = sorted(kwargs.items(), key=lambda kvp: -len(kvp[1]))
	sorted_dict = dict(sorted_lst)
	return sorted_dict

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))

