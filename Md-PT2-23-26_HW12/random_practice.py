import random

# 1
# print(f"Результат броска кубика :{random.randint(1, 6)}")

# 2
# s = "abcdefghijklmnopqrstuvwxyz"
# password = "".join(random.choices(s, k=8))
# print(f"Случайный пароль из 8 символов: {password}")


# 3
# def http_random():
#     HTTP_list = ["GET", "POST", "PUT", "DELETE"]
#     return random.choice(HTTP_list)


# print(http_random())

# 4
# tests = ["test_login", "test_logout", "test_add_to_cart", "test_checkout"]
# random.shuffle(tests)
# print(f"Новый перемешанный список: {tests}")

# 5
# users = ["alice", "bob", "carol", "dave", "erin"]
# print(f"2 случайных пользователья из списка: {random.sample(users, 2)}")


# 6
# def run_flaky_test():
#     if random.random() < 0.3:
#         return "FAILED"
#     else:
#         return "PASSED"


# print(run_flaky_test())

# 7

# print(f"Лотерейный билет из 6 уникальных чисел: {random.sample(range(1, 50), k = 6)}")


# 8
# def generate_test_data(n):
#     return random.choices(range(0, 101), k=n)


# print(generate_test_data(3))
