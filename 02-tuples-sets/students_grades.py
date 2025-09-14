num_of_students = int(input())
students = {}

for _ in range(num_of_students):
	student_name, grade = input().split()
	if student_name not in students:
		students[student_name] = []
	students[student_name].append(float(grade))

for name, grades in students.items():
	avg_grade = sum(grades) / len(grades)
	print(f"{name} -> {' '.join([f'{el:.2f}' for el in grades])} (avg:"
		  f" {avg_grade:.2f})")
