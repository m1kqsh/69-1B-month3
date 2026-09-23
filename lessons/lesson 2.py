# # родительский класс, суперкласс
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
#
# # дочерний класс, наследник, подкласс
# class ElectricCar(Car):
#     def __init__(self, color, model, battery, max_speed=100):
#         super().__init__(color, model, max_speed)
#         self.battery = battery
#
#     def charge(self):
#         self.battery += 25
#         if self.battery > 100:
#             self.battery = 100
#
#     def drive_to(self, destination):
#         self.battery -= 5
#         if self.battery < 0:
#             self.battery = 0
#         print(f"Электрокар марки {self.model} едет в {destination}, "
#                 f"батарея {self.battery}%")
#
# car_1 = Car("red", "Kia", 170)
# car_2 = Car("black", "Subaru", 180)
# el_car_1 = ElectricCar("black", "Tesla", 95, 250)
# print(el_car_1.model, el_car_1.battery, el_car_1.max_speed)
# el_car_1.drive_to("Кант")
# el_car_1.charge()
# print(el_car_1.battery)
# el_car_1.drive_to("Бишкек")
# print(el_car_1.battery)