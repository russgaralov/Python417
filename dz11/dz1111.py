def averagedecorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        average = sum(result) / len(result)
        print(f"Сумма чисел: {sum(result)}")
        print(f"Среднее арифметическое чисел: {average}")
        return result
    return wrapper

@averagedecorator
def getnumbers():
    return [2, 3, 3, 4]
getnumbers()