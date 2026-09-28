# 1
# import time


# def retry(times):
#     def decorator(func):
#         def wrapper(**kwargs):
#             for i in range(1, times + 1):
#                 res = func(**kwargs)
#                 if res == "FAILURE":
#                     print(f"Не успешно! попытка номер {i}")
#                 else:
#                     return res
#             return "Попыток больше нет"

#         return wrapper

#     return decorator


# @retry(times=2)
# def flaky_test():
#     if time.time() % 2 < 1:
#         return "FAILURE"
#     return "PASSED"


# print(flaky_test())


# 2
# def require_role(required_role):
#     def decor(func):
#         def wrapper(*args):
#             print(
#                 "Выполняется админский тест"
#             )  # перенес это строку сюда, чтобы эта строка писалась в любом случае
#             user_role = args[0]
#             if user_role == required_role:
#                 return func(*args)
#             else:
#                 return f"Ошибка: Требуется роль {required_role}, текущая: {user_role}"

#         return wrapper

#     return decor


# user_one = "user"
# user_two = "admin"


# @require_role("admin")
# def admin_test(*args):
#     return "Success"


# print(admin_test(user_one))

# 3
# import time


# def timer(func):
#     def wrapper(*args):
#         start_time = time.time()
#         res = func(*args)
#         end_time = time.time()
#         work_time = end_time - start_time
#         print(f"{func.__name__} выполнился за {work_time:.2f} сек.")
#         return res

#     return wrapper


# @timer
# def slow_test():
#     time.sleep(1)
#     return "OK"


# print(slow_test())

# 4
# import time


# def wait_with_retry_until(timeout=10, interval=0.5):
#     def decor(func):
#         def wrapper():
#             end_time = time.time() + timeout
#             attempt = 1
#             while time.time() < end_time:
#                 success = func()
#                 print(f"Попытка {attempt}: {'успешно' if success else 'неуспешно'}")

#                 if success:
#                     print("Элемент найден")
#                     return True
#                 attempt += 1
#                 time.sleep(interval)
#             return False

#         return wrapper

#     return decor


# @wait_with_retry_until(timeout=3, interval=0.5)
# def element_visible():
#     return time.time() % 3 > 2


# element_visible()

# 5
# import time
# from functools import wraps


# def count_exec_time(func):
#     @wraps(func)
#     def wrapper(n):
#         print(f"Выполняю {func.__name__} с аргументом {n}")
#         start_time = time.time()
#         result = func(n)
#         end_time = time.time()
#         print(f"Время выполнения: {end_time-start_time}")
#         return result

#     return wrapper


# def cache_results(func):
#     cache = {}

#     @wraps(func)
#     def wrapper(n):
#         if n not in cache:
#             cache[n] = func(n)
#             print(cache[n])
#         return cache[n]

#     return wrapper


# @count_exec_time
# @cache_results
# def expensive_calculation(n):
#     print(f"Вычисляем для {n}")
#     time.sleep(1)
#     return n * n


# expensive_calculation(7)


# 6
# def validate_params(examination):
#     def decor(func):
#         def wrapper(**kwargs):
#             if type(kwargs["username"]) != str:
#                 return "username должен быть str"
#             if type(kwargs["age"]) != int:
#                 return "age должен  быть int"
#             return func(**kwargs)

#         return wrapper

#     return decor


# @validate_params({"username": str, "age": int})
# def create_user(**kwargs):
#     return f"Пользователь {kwargs['username']} создан"


# print(create_user(username="test", age=25))
# print(create_user(username="test", age="25"))

# 7
# LOG_LEVEL = "DEBUG"
# LEVELS = {"DEBUG": 10, "INFO": 20, "WARNING": 30, "ERROR": 40}


# def conditional_log(min_level="INFO"):
#     def decor(func):
#         def wrapper():
#             current_weight = LEVELS[LOG_LEVEL]
#             required_weight = LEVELS[min_level]

#             if current_weight >= required_weight:
#                 print(f"[{min_level}] Вызов функции {func.__name__}")
#             return func()

#         return wrapper

#     return decor


# @conditional_log("DEBUG")
# def debug_test():
#     return "debug_result"


# debug_test()
