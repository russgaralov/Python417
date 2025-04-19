
students = [
    {"name": "Игорь", "score": 12},
    {"name": "Валентин", "score": 7},
    {"name": "Виктор", "score": 4},
    {"name": "Григорий", "score": 9},
    {"name": "Дмитрий", "score": 6}
]


total_score = sum(student["score"] for student in students)
average_score = total_score / len(students)


above_average_students = [student["name"] for student in students if student["score"] > average_score]


print("Средний балл:", average_score)
print("Студенты с баллом выше среднего:", above_average_students)
