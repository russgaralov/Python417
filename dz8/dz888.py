
sales = {
    "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
    "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
    "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
    "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}
}


name = input("Имя: ")
region = input("Регион: ")


print(sales[name][region])


new_value = int(input("Новое значение: "))
sales[name][region] = new_value


print(sales[name])
