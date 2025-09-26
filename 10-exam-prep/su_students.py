def softuni_students(*args, **kwargs):
	students_dict = {}
	non_assigned_students = []
	for course_id, student in args:
		if course_id in kwargs:
			students_dict[student] = kwargs[course_id]
		else:
			non_assigned_students.append(student)
	
	sorted_assigned_students = sorted(students_dict.items(),
									  key=lambda kvp: kvp[0])
	
	output = []
	for student, course in sorted_assigned_students:
		output.append(
			f"*** A student with the username {student} has successfully "
			f"finished the course {course}!")
	
	if non_assigned_students:
		sorted_non_assigned_students = sorted(non_assigned_students)
		output.append(
			f"!!! Invalid course students: "
			f"{', '.join(sorted_non_assigned_students)}")
	
	return "\n".join(output)


# print(softuni_students(
# 	('id_1', 'Kaloyan9905'),
# 	id_1='Python Web Framework',
# ))

# print(softuni_students(
# 	('id_7', 'Silvester1'),
# 	('id_32', 'Katq21'),
# 	('id_7', 'The programmer'),
# 	id_76='Spring Fundamentals',
# 	id_7='Spring Advanced',
# ))

print(softuni_students(
	('id_22', 'Programmingkitten'),
	('id_11', 'MitkoTheDark'),
	('id_321', 'Bobosa253'),
	('id_08', 'KrasimirAtanasov'),
	('id_32', 'DaniBG'),
	id_321='HTML & CSS',
	id_22='Machine Learning',
	id_08='JS Advanced',
))
