number = input("Введите пятизначное число: ")

if len(number) != 5 or not number.isdigit():
    print("Ошибка: Введите ровно пять цифр.")
else:
    digits = [int(c) for c in number]
    product = 1
    for d in digits:
        product *= d
    average = sum(digits) / 5
    print(f"Произведение цифр числа {number}: {product}")
    print(f"Среднее арифметическое: {average}")
