# 1.1
# class Product:
#     def __init__(self, price):
#         if price >= 0:
#             self._price = price
#         else:
#             print("Отрицательную цену задать нельзя")
#             self._price = 0

#     @property
#     def price(self):
#         return self._price

#     @price.setter
#     def price(self, value):
#         if value >= 0:
#             self._price = value
#         else:
#             print("Отрицательную цену задать нельзя")


# p = Product(100)
# print(p.price)

# p.price = 250
# print(p.price)

# p.price = -10
# print(p.price)


# 1.2
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     @property
#     def area(self):
#         return self.length * self.width


# rect = Rectangle(3, 4)
# print(rect.area)

# rect.width = 10
# print(rect.area)


# 1.3
# class TestStats:
#     def __init__(self, passed, total):
#         self.passed = passed
#         self.total = total

#     @property
#     def success_rate(self):
#         return (self.passed / self.total) * 100


# stats = TestStats(8, 10)
# print(stats.success_rate)
# stats.passed = 9
# print(stats.success_rate)


# 2.1
# class PermissionMixin:
#     def has_permission(self, user_role):
#         return user_role == "admin"


# class SecureAction(PermissionMixin):
#     def execute(self, role):
#         if self.has_permission(role):
#             print("Админ. Метод запущен")
#         else:
#             print("Нет прав.")


# action = SecureAction()
# action.execute("user")
# action.execute("admin")


# 2.2
# class Logger:
#     def log(self, message):
#         print(f"[Log] {message}")


# class Service(Logger):
#     def __init__(self):
#         self.logger = Logger()

#     def process(self):
#         self.logger.log("Начал обработку")
#         print("Обрабатываю")
#         self.logger.log("Закончил обработку")


# s = Service()
# s.process()


# 2.3
# class Admin:
#     def create_user(self, user):
#         print(f"Пользователь c именем {user} создан")


# class Support:
#     def create_ticket(self, ticket):
#         print(f"Тикет '{ticket}' создан")


# class SuperUser(Admin, Support):
#     pass


# su = SuperUser()
# su.create_user("Ivan")
# su.create_ticket("Падает сервис")


# 2.4
# class A:
#     def who_am_i(self):
#         print("A")


# class B(A):
#     def who_am_i(self):
#         print("В")


# class C(A):
#     def who_am_i(self):
#         print("С")


# class D(B, C):
#     pass


# d = D()
# d.who_am_i()
# print(D.mro())


# 2.5
# class LogginMixin:
#     def log(self):
#         print("[LOG] Выполняем задачу")


# class RetryMixin:
#     def retry(self, attemps):
#         for i in range(1, attemps + 1):
#             print(f"Попытка {i}")
#             self.run()


# class Job(LogginMixin, RetryMixin):
#     def run(self):
#         self.log()
#         print("Job что-то делает...")


# j = Job()
# j.retry(4)

# 3.1
# from abc import ABC, abstractmethod
# import math


# class Shape:
#     @abstractmethod
#     def area(self):
#         pass


# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return f"Прямоугольник. Площадь: {self.length * self.width}"


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return f"Круг. Площадь:{math.pi * (self.radius ** 2):.2f}"


# shapes = [Rectangle(3, 4), Circle(2)]
# for s in shapes:
#     print(s.area())

# 3.2
# from abc import ABC, abstractmethod


# class Transport:
#     @abstractmethod
#     def move(self):
#         pass

#     def go(self):
#         print("Начинаем движение")
#         self.move()


# class Car(Transport):
#     def move(self):
#         print("Едем по дороге на машине")


# class Bike(Transport):
#     def move(self):
#         print("Едем по дороге на велосипеде")


# for t in (Car(), Bike()):
#     t.go()

# 3.3
# from abc import ABC, abstractmethod


# class BaseTestCase:
#     @abstractmethod
#     def prepare_data(self):
#         pass

#     @abstractmethod
#     def run_test():
#         pass

#     def run(self):
#         self.prepare_data()
#         self.run_test()


# class LoginTest(BaseTestCase):
#     def prepare_data(self):
#         print("===LoginTest===")
#         print("Готовим пользователя для логина")

#     def run_test(self):
#         print("Проверяем успешный пароль")


# class PaymentTest(BaseTestCase):
#     def prepare_data(self):
#         print("===PaymentTest===")
#         print("Готовим данные карты и баланс")

#     def run_test(self):
#         print("Проверяем успешный платеж")


# tests = [LoginTest(), PaymentTest()]
# for t in tests:
#     t.run()


# 4.1
# class BaseTest:
#     def run(self):
#         pass


# class APITest(BaseTest):
#     def __init__(self, endpoint):
#         self.endpoint = endpoint

#     def run(self):
#         print(f"API тест: проверяем эндпоинт {self.endpoint}")


# class UITest(BaseTest):
#     def __init__(self, page):
#         self.page = page

#     def run(self):
#         print(f"UI тест: проверяем страницу {self.page}")


# def run_all(tests):
#     for t in tests:
#         t.run()


# tests = [
#     APITest("/login"),
#     UITest("LoginPage"),
#     APITest("/users"),
# ]
# run_all(tests)


# 4.2
# def print_length(obj):
#     print(len(obj))


# class TestCollection:
#     def __init__(self, data):
#         self.data = data

#     def __len__(self):
#         return len(self.data)


# print_length("Python")
# print_length([1, 2, 3])
# print_length({"a": 1, "b": 2})
# print_length(TestCollection([10, 20, 30, 40]))
