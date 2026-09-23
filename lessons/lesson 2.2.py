# class Car:
#     def __init__(self, color, model, max_speed=100):
#         # слева self.color — атрибут объекта, справа color — параметр.
#         # сохраняем переданное значение внутрь объекта
#         self.color = color
#         self.model = model
#         self.max_speed = max_speed
#
#     def drive_to(self, destination):
#         print(f"Машина марки {self.model} и цвета {self.color} едет в {destination}")
#
# class ElectricCar(Car):
#     def drive_to(self, destination):
#         print(f"Электрокар марки {self.model} едет в {destination}")
#
# class SportCar(Car):
#     def drive_to(self, destination):
#         print(f"Спорткар марки {self.model} едет в {destination}")
#
# car_1 = Car("black", "Subaru", 180)
# el_car_1 = ElectricCar("black", "Tesla", 250)
# sport_car_1 = SportCar("red", "Honda", 320)
#
# cars = [car_1, el_car_1, sport_car_1]
# for c in cars:
#     c.drive_to("Кант")
#
# car_1.drive_to("Кант")
# el_car_1.drive_to("Кант")
# sport_car_1.drive_to("Кант")