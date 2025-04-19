n = int(input("Введите число от 1 до 99: "))

if 11 <= n % 100 <= 14:
    suffix = "копеек"
else:
    last_digit = n % 10
    if last_digit == 1:
        suffix = "копейка"
    elif 2 <= last_digit <= 4:
        suffix = "копейки"
    else:
        suffix = "копеек"

print(f"{n} {suffix}")