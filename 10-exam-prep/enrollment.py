def gather_credits(needed_credits: int, *courses_credits):
	courses: list[str] = []
	credits_now = 0
	
	for course, credits in courses_credits:
		if credits_now >= needed_credits:
			break
		
		if course not in courses:
			courses.append(course)
			credits_now += credits
	
	sorted_courses = sorted(courses)
	result = ""
	if credits_now >= needed_credits:
		result = f"Enrollment finished! Maximum credits: {credits_now}.\n"
		result += f"Courses: {', '.join(sorted_courses)}"
	
	else:
		result = f"You need to enroll in more courses! You have to gather {needed_credits - credits_now} credits more."
	
	return result


# print(gather_credits(80, ("Basics", 27), ))

# print(gather_credits(80, ("Advanced", 30), ("Basics", 27),
# 	("Fundamentals", 27), ))

print(gather_credits(60, ("Basics", 27), ("Fundamentals", 27), ("Advanced", 30),
	("Web", 30)))
