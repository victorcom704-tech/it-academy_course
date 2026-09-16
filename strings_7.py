user_string = input("Введите строку: ")
if user_string.replace(" ", "").isdigit():
    print("Строка состоит только из цифр - True")
else:
    print("Строка не состоит только из цифр - False")
