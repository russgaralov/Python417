
numbers = [6, 3, 0, 8, 2]

non_zero_numbers = [num for num in numbers if num != 0]


average = sum(non_zero_numbers) / len(non_zero_numbers)

print("Среднее арифметическое ненулевых элементов:", average)
