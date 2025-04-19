
elements = [-3,5,-1, 9, 3, 4, -5]


positive_elements = []
for element in elements:
    if element > 0:
        positive_elements.append(element)


print("Новый список, состоящий из положительных элементов:")
print(positive_elements)


max_element = max(positive_elements)


print("\nНаибольший элемент списка:", max_element)
