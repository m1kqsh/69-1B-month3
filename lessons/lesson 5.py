# from abc import ABC, abstractmethod  # ABC — базовый класс для абстрактных, @abstractmethod — декоратор
#
# # Абстрактные классы (ABC) и абстрактные методы (@abstractmethod).
# # Абстрактный класс нельзя создать напрямую — он описывает интерфейс,
# # а конкретные классы-наследники должны реализовать все абстрактные методы.
#
#
# class Animal(ABC):  # абстрактный класс — "шаблон" для наследников
#     @abstractmethod  # метод ОБЯЗАН быть переопределён в наследниках
#     def make_sound(self):
#         pass
#
#     @abstractmethod  # метод ОБЯЗАН быть переопределён в наследниках
#     def test(self):
#         pass
#
#
# # animal1 = Animal()  # Ошибка: абстрактный класс нельзя создать напрямую
#
# class Dog(Animal):  # конкретная реализация — переопределяет все абстрактные методы
#     def make_sound(self):
#         print("Гав гав")
#
#     def test(self):
#         print("test dog")
#
#
# class Cat(Animal):  # НЕПОЛНАЯ реализация — не переопределён метод test
#     def make_sound(self):
#         print("Мяяяяяяяу")
#
#     # def test(self):
#     #     print("test cat")
#
#
# puppy = Dog()
# puppy.make_sound()
# # kitty = Cat()  # Ошибка: Cat не реализовал обязательный абстрактный метод test