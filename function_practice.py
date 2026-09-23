# 1
# def calculator(num1, num2):
#     operation = input("Выберите операцию () +, -, /, * или **) или выход: ")
#     if operation == "+":
#         print("Вы выбрали сумму")
#         print(f"Результат: {num1} + {num2} = {num1 + num2}")
#     elif operation == "-":
#         print("Вы выбрали вычитание")
#         print(f"Результат: {num1} - {num2} = {num1 - num2}")
#     elif operation == "/":
#         print("Вы выбрали деление")
#         if num2 == 0:
#             print("Лучше не надо делить на 0")
#         else:
#             print(f"Результат: {num1} / {num2} = {num1 / num2}")
#     elif operation == "*":
#         print("Вы выбрали умножение")
#         print(f"Результат: {num1} * {num2} = {num1 * num2}")
#     elif operation == "**":
#         print("Вы выбрали возведение в степень")
#         print(f"Результат возведение числа {num1} в степень {num2} равна {num1**num2}")
#     else:
#         print("Некорректная операция!\nРезультат: None")


# calculator(
#     float(input("Введите первое число: ")), float(input("Введите второе число: "))
# )

# 2.1
# test_results = [
#     {"name": "login_test", "status": "passed", "duration": 2.1},
#     {"name": "payment_test", "status": "failed", "duration": 3.5},
#     {"name": "logout_test", "status": "passed", "duration": 1.2},
# ]
# test_status_passed = list(filter(lambda test: test["status"] == "passed", test_results))
# test_name_passed = [test["name"] for test in test_status_passed]
# print(f"Успешные тесты: {test_name_passed}")

# 2.2
# tests = [
#     {"name": "complex_test", "duration": 5.2},
#     {"name": "simple_test", "duration": 1.1},
#     {"name": "medium_test", "duration": 3.4},
# ]
# tests.sort(key=lambda test: test["duration"])
# print(f"Тесты по времени выполнения: {tests}")

# 2.3
# emails = ["test@gmail.com", "invalid-email", "user@company.ru", "no@domain"]
# valid_emails = list(
#     filter(lambda email: "@" in email and email.endswith((".ru", ".com")), emails)
# )
# print(f"Валидные email: {valid_emails}")


# 3.1
# def apply_test_check(check_func, test_results):
#     passed_count = len(list(filter(check_func, test_results)))
#     return passed_count


# test_results = [{"status": "passed"}, {"status": "failed"}, {"status": "passed"}]

# result = apply_test_check(lambda test: test["status"] == "passed", test_results)
# print(f"Прошло тестов: {result}")


# 3.2
# def filter_logs(logs, filter_func):
#     return [log for log in logs if filter_func(log)]


# logs = [
#     {"level": "INFO", "message": "Test started"},
#     {"level": "ERROR", "message": "Login failed"},
#     {"level": "WARNING", "message": "Timeout occurred"},
# ]

# error_logs = filter_logs(logs, lambda level: level["level"].lower() == "error")
# print("Ошибки:", error_logs)


# 3.3
# def transform_tests(tests, transform_func):
#     return [transform_func(test) for test in tests]


# tests = [{"name": "test1", "duration": 2.0}, {"name": "test2", "duration": 3.0}]
# increased_tests = transform_tests(
#     tests, lambda t: {**t, "duration": t["duration"] * 1.1}
# )
# print("Тесты с увеличенным временем:", increased_tests)


# 4.1
# def generate_report(title, *test_names, format="html", **options):
#     print(f"Отчёт: {title}")
#     print(f"Формат: {format}")
#     print(f"Тесты: {', '.join(test_names)}")
#     for key, value in options.items():
#         print(f"{key}:{value}")


# generate_report(
#     "Daily Report", "test1", "test2", "test3", format="pdf", author="Tester"
# )
