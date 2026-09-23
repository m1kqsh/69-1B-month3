# class Car:
#     # __init__ — конструктор. Python вызывает его САМ при создании объекта (когда пишем Car(...))
#     # self — это сам создаваемый объект. При вызове мы его НЕ передаём, Python подставляет сам
#     def __init__(self, color, model, max_speed=100):
#         # слева self.color — атрибут объекта, справа color — параметр.
#         # сохраняем переданное значение внутрь объекта
#         self.color = color
#         self.model = model
#         self.max_speed = max_speed
#
#     # через self метод получает доступ к атрибутам СВОЕГО объекта (self.model, self.color)
#     def drive_to(self, destination):
#         print(f"Машина марки {self.model} и цвета {self.color} едет в {destination}")
#
#     def change_color(self, new_color):
#         self.color = new_color
#
# # класс для игрового персонажа, добавить любые свойства на усмотрение
# # и создать 1-2 объекта
# class GameCharacter:
#     pass
#
# car_1 = Car("red", "Kia", 170)
# car_2 = Car("black", "Subaru", 180)
# print(car_1)
# print(car_2)
# print(car_1.color)
# print(car_2.color)
# car_1.drive_to("Каракол")
# car_2.color = "white"
# print(car_2.color)
# car_2.fined = True
# print("оштрафован?", car_2.fined)
# # print(car_1.fined) # тут будет ошибка, так как у объектов Car нет такого свойства
# car_1.change_color("silver")
# print(car_1.color)