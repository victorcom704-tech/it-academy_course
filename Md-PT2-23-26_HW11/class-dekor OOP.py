# 1
# def test_info(author, component):
#     def decor(cls):
#         cls.author = author
#         cls.component = component
#         return cls

#     return decor


# @test_info(author="Иван", component="Auth")
# class TestLogin:
#     pass


# print(TestLogin.author)
# print(TestLogin.component)

# 2
# PAGES = []


# def register_page(cls):
#     PAGES.append(cls)
#     return cls


# @register_page
# class PageCreate:
#     pass


# @register_page
# class PageDelete:
#     pass


# print([cls.__name__ for cls in PAGES])


# 3
# class Tag_name:
#     def __init__(self, tag):
#         self.tag = tag

#     def __call__(self, cls):
#         cls.tag = self.tag
#         return cls


# @Tag_name("smoke")
# class SmokeTests:
#     pass


# @Tag_name("regression")
# class RegressionTests:
#     pass


# print(SmokeTests.tag)
# print(RegressionTests.tag)

# 4
# from enum import Enum


# class Environment(Enum):
#     DEV = "https://dev.example.com"
#     STAGE = "https://stage.example.com"
#     PROD = "https://example.com"


# def get_base_url(site):
#     return site.value


# print(get_base_url(Environment.DEV))
# print(get_base_url(Environment.PROD))

# 5
# from enum import Enum


# class Priority(Enum):
#     LOW = 1
#     MEDIUM = 2
#     HIGH = 3


# tasks = [
#     ("Починить тест логина", Priority.HIGH),
#     ("Обновить документацию", Priority.LOW),
#     ("Настроить CI", Priority.MEDIUM),
# ]

# tasks_sorted = sorted(tasks, key=lambda x: x[1].value)

# for name, prio in tasks_sorted:
#     print(prio.name, "-", name)

# 6
# from enum import Enum


# class TestType(Enum):
#     API = "API"
#     UI = "UI"
#     UNIT = "UNIT"


# tests = [
#     ("test_login_api", TestType.API),
#     ("test_login_ui", TestType.UI),
#     ("test_sum", TestType.UNIT),
#     ("test_profile_api", TestType.API),
# ]


# def filter_tests_by_type(tests, test_type: TestType):
#     res = []
#     for name, x in tests:
#         if x == test_type:
#             res.append(name)
#     return res

# print(filter_tests_by_type(tests, TestType.API))
# print(filter_tests_by_type(tests, TestType.UI))


# 7
# def parse_int_list(strings):
#     res = []
#     for x in strings:
#         try:
#             num = int(x)
#             res.append(num)
#         except ValueError:
#             print(f"{x} не является целым числом")
#     return res


# raw = ["10", "20", "abc", "30", "4.5", "40"]
# nums = parse_int_list(raw)
# print(nums)


# 8
# def calc(x, y, operation):
#     try:
#         if operation not in ("+", "-", "*", "/"):
#             raise ValueError(f"Неизвестная операция")
#         if operation == "+":
#             return x + y
#         if operation == "-":
#             return x - y
#         if operation == "*":
#             return x * y
#         if operation == "/":
#             return x / y
#     except ZeroDivisionError:
#         return "Делить на ноль нельзя"
#     except TypeError:
#         return "Неверный ввод"


# try:
#     print(calc(6, 3, "/"))
#     print(calc(7, 0, "/"))
#     print(calc("10", 5, "+"))
#     print(calc(10, 5, "фывфы"))
# except ValueError as error:
#     print(f"Ошибка снаружи: {error}")

# 9
# from dataclasses import dataclass
# @dataclass(frozen=False)
# class Point:
#     x: float
#     y: float


# p1 = Point(1.0, 2.0)
# p2 = Point(-3.5, 4.2)
# print(p1)
# print(p2)

# 10
# from dataclasses import dataclass


# @dataclass
# class Product:
#     name: str
#     price: float
#     quantity: int = 1

#     def total(self):
#         return self.price * self.quantity


# p1 = Product("Keyboard", 50.0, 2)
# p2 = Product("Mouse", 25.0)

# print(p1, "total:", p1.total())
# print(p2, "total:", p2.total())

# 11
# from dataclasses import dataclass, field
# from typing import List, Optional


# @dataclass
# class Book:
#     title: str
#     authors: list[str] = field(default_factory=list)
#     year: int | None = None

#     def formatted(self):
#         authors_str = ", ".join(self.authors)
#         year_str = f"({self.year})" if self.year is not None else ""
#         return f'"{self.title}" {year_str} - {authors_str}'


# b1 = Book("Python 101", ["John Doe"], 2020)
# b2 = Book("Безымянная книга")
# b3 = Book("Совместный труд", ["Alice", "Bob"])

# for b in (b1, b2, b3):
#     print(b.formatted())
