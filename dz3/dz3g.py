try:
    n = int(input("Введите количество символов: "))
    if n <= 0:
        print("Ошибка: количество символов должно быть положительным.")
        exit()
except ValueError:
    print("Ошибка: введите целое число для количества символов.")
    exit()

char = input("Введите тип символа: ")
if len(char) != 1:
    print("Ошибка: введите ровно один символ.")
    exit()

orientation = input("Введите ориентацию линии (@ - горизонтальная, 1 - вертикальная): ")
if orientation not in ['@', '1']:
    print("Ошибка: ориентация должна быть '@' или '1'.")
    exit()

if orientation == '@':
    print(char * n)
else:
    for _ in range(n):
        print(char)