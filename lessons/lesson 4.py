# # Атрибуты класса (общие для всех объектов) и методы класса (@classmethod).
# # cls — это сам класс (аналог self, но для класса, а не объекта).
#
# class User:
#     user_count = 0              # атрибут класса: ОДИН на все объекты, общий счётчик
#     default_password = "123456" # тоже общий — значение по умолчанию для всех
#
#     def __init__(self, name, phone_number):
#         self.name = name
#         self.phone_number = phone_number
#         self.password = User.default_password   # читаем общий атрибут через имя класса
#         self.role = "user"
#         User.user_count += 1   # при создании каждого объекта увеличиваем ОБЩИЙ счётчик
#
#     def change_password(self, new_password):
#         if User.validate_password(new_password):
#             # проверка пароля прошла
#             self.password = new_password
#         else:
#             # проверка пароля НЕ прошла
#             raise ValueError("Password is too short")
#
#     @classmethod
#     def get_user_count(cls):
#         # cls — это сам класс (как self, но для класса). self здесь не нужен.
#         return cls.user_count
#
#     @classmethod
#     def create_admin(cls, name, phone_number):
#         # альтернативный конструктор: создаёт объект с правами админа.
#         # cls(...) вызывает обычный __init__; лучше писать cls, а не User,
#         # чтобы работал и для классов-наследников.
#         obj = cls(name, phone_number)
#         obj.role = "admin"
#         obj.change_password("qwerty123456")
#         return obj
#
#     @staticmethod
#     def validate_password(password):
#         # статический метод: не получает ни self, ни cls.
#         # Работает как обычная функция, просто "живёт" в классе.
#         # if len(password) < 10:
#         #     return False
#         # else:
#         #     return True
#         return len(password) >= 10
#
# print(User.user_count)
# user1 = User("Igor", "996555000000")
# print(user1.name, user1.phone_number)
# user1.change_password("qwerty1234")  # ровно 10 символов — минимально допустимый пароль
# print(User.user_count)
# user2 = User("Kurmanbek", "996555000001")
# print(User.get_user_count())
# admin1 = User.create_admin("Arseniy", "996555000002")
# print(admin1.name, admin1.role)
# print(User.validate_password("12345654321"))  # прямая проверка валидации