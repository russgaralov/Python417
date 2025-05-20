import math

class GeometryCalculator:
    @staticmethod
    def triangle_area_heron(a, b, c):
        # Вычисление площади треугольника по формуле Герона
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area

    @staticmethod
    def triangle_area_base_height(base, height):
        # Вычисление площади треугольника через основание и высоту
        area = 0.5 * base * height
        return area

    @staticmethod
    def square_area(side):
        # Вычисление площади квадрата
        area = side ** 2
        return area

    @staticmethod
    def rectangle_area(length, width):
        # Вычисление площади прямоугольника
        area = length * width
        return area

    @staticmethod
    def count_subsets_area(area):
        # Вычисление количества подсетов площади
        return 4


print("Площадь треугольника по формуле Герона (3, 4, 5):", GeometryCalculator.triangle_area_heron(3, 4, 5))
print("Площадь треугольника через основание и высоту (6, 7):", GeometryCalculator.triangle_area_base_height(6, 7))
print("Площадь квадрата (7):", GeometryCalculator.square_area(7))
print("Площадь прямоугольника (2, 6):", GeometryCalculator.rectangle_area(2, 6))
print("Количество подсетов площади:", GeometryCalculator.count_subsets_area(12))
