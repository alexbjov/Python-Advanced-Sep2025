def students_credits(*args):
    courses_credits: dict[str, float] = {}
    target_credits = 240
    result: list[str] = []

    for data in args:
        course, max_credits, max_points, won_points = data.split("-")
        won_credits = int(won_points) / int(max_points) * int(max_credits)
        courses_credits[course] = won_credits

    total_won_credits = sum(courses_credits.values())
    if total_won_credits >= target_credits:
        result.append(f"Diyan gets a diploma with {total_won_credits:.1f} credits.")
    else:
        result.append(f"Diyan needs {target_credits - total_won_credits:.1f} credits more for a diploma.")

    sorted_courses = sorted(courses_credits.items(), key=lambda x: -x[1])
    for course, credits in sorted_courses:
        result.append(f"{course} - {credits:.1f}")

    return "\n".join(result)

# print(
#     students_credits(
#         "Computer Science-12-300-250",
#         "Basic Algebra-15-400-200",
#         "Algorithms-25-500-490"
#     )
# )

# print(
#     students_credits(
#         "Discrete Maths-40-500-450",
#         "AI Development-20-400-400",
#         "Algorithms Advanced-50-700-630",
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Game Engine Development-70-100-70",
#         "Mobile Development-25-250-225",
#         "QA-20-300-300",
#     )
# )

# print(
#     students_credits(
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Java Development-10-300-150"
#     )
# )
