class Human:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} лет"

class Student(Human):
    def __init__(self, first_name, last_name, age, course):
        super().__init__(first_name, last_name, age)
        self.course = course

    def __str__(self):
        return f"{super().__str__()}, студент {self.course} курса"

class Teacher(Human):
    def __init__(self, first_name, last_name, age, subject):
        super().__init__(first_name, last_name, age)
        self.subject = subject

    def __str__(self):
        return f"{super().__str__()}, преподаватель {self.subject}"

class Graduate(Student):
    def __init__(self, first_name, last_name, age, course, diploma):
        super().__init__(first_name, last_name, age, course)
        self.diploma = diploma

    def __str__(self):
        return f"{super().__str__()}, выпускник с дипломом {self.diploma}"

# Создание списка групп
group = [
    Student("Батодалаев", "Даши", 16, "ГК Web_011"),
    Student("Шугани", "Сергей", 15, "РПО PD_011"),
    Student("Данилин", "Андрей", 38, "Астрономия 110"),
    Student("Маркин", "Даниил", 17, "ГК Python_011"),
    Graduate("Баширов", "Алексей", 45, "Разработка приложений", "20")
]

# Вывод информации о каждом участнике
for member in group:
    print(member)
