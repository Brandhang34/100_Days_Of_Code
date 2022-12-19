# new_numbers = [num * 2 for num in range (1,5)]
# print(new_numbers)

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]

# print(short_names)

# long_names = [name.upper() for name in names if len(name) >= 5]
# print(long_names)

import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_scores = {student: random.randint(1, 100) for student in names}

passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}

print(students_scores)

print(passed_students)
