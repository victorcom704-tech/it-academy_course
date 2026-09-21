# 1
# user_string = input("Введите строку: ")
# for char in user_string:
#     print(char)

# 2
# user_string = input("Введите строку: ")
# vowels = "уеыаоэяиюёaeiou"
# cnt = 0
# for char in user_string:
#     if char.lower() in vowels:
#         cnt += 1
# print(f"Количество гласных = {cnt}")

# 3
# user_string = input("Введите несколько тестовых названий(через пробел): ").split()
# for case in user_string:
#     print(f' "Test case: {case}"')

# 4
# password = "admin"
# while True:
#     user_password = input("Введите пароль: ")
#     if user_password == password:
#         print("Пароль верный!")
#         break
#     else:
#         print("Пароль неверный, попробуй еще раз")

# 5
# for num in range(1, 11):
#     if num % 3 == 0:
#         continue
#     print(num)

# 6
# res = 0
# for num in range(1, 101):
#     res += num
# print('Сумма равна', res)

# 7
# browsers = ["Chrome", "Firefox"]
# operating_system = ["Windows", "Linux"]
# for browsers in browsers:
#     for os in operating_system:
#         print(f'"{browsers}-{os}"')

# 8
# user_string = input('Введите строку: ')
# for i, char in enumerate(user_string):
#     print(f'Индекс: {i}, символ строки: {char}')

# 9
# user_email = input('Ввидте email: ')
# for sym in user_email:
#     if sym == "@":
#         print('Есть символ @')
#         break
# else:
#     print('Нет символа @')

# 10
# num = 10
# while num >= 0:
#     print(num)
#     num -= 1

# 11
# res = ""
# user_string = input("Введите строку: ")
# for char in user_string:
#     res += char.upper()
# print(res)

# 12
# while True:
#     num = int(input("Введите число: "))
#     if num > 10:
#         print("Хватит")
#         break
#     else:
#         print("Давай ещё раз")

# 13
# print("Количество слов в строке:", len(input("Введите строку: ").split()))

# 14
# for num in range(21):
#     print(num)
#     if num == 15:
#         break
