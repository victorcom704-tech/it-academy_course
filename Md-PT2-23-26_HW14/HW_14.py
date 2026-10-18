# 5
# def log_message(path, message):
#     with open(path, "a") as f:
#         f.write(f"{message}\n")


# log_message("app.log", "Test started")
# log_message("app.log", "Test finished")


# 6
# def read_first_chars(path, n):
#     with open(path, "r") as f:
#         return f.read(n)


# print(read_first_chars("app.log", 5))
# print(read_first_chars("app.log", 100))


# 7
# def filter_file(src, dst, keyword):
#     try:
#         with open(src, "r") as f_1, open(dst, "w") as f_2:
#             for l in f_1:
#                 if keyword in l:
#                     f_2.write(l)
#     except FileNotFoundError:
#         print(f"Файл {src} не обнаружен")


# filter_file("app.log", "errors.log", "ERROR")


# 8
# def sums(path):
#     total = 0
#     try:
#         with open(path, "r") as f:
#             for l in f:
#                 total += int(l)
#     except FileNotFoundError:
#         return 0

#     return total


# assert sums("numbers.txt") == 1 + 2 + 3 + 4 + 5
# print("Проверка пройдена")


# 9
# def copy_binary(src, dst):
#     try:
#         with open(src, "rb") as f_1, open(dst, "wb") as f_2:
#             f_2.write(f_1.read())
#         print("Файл скопирован")
#     except FileNotFoundError:
#         print("Файл не обнаружен")


# copy_binary("image.png", "image_copy.png")
# copy_binary("asd.png", "asd_copy.png")


# 10
# def read_config(path):
#     res = {}
#     try:
#         with open(path, "r") as f:
#             for l in f:
#                 if l == "\n" or l == "":
#                     continue
#                 if l.startswith("#"):
#                     continue
#                 if "=" in l:
#                     key, value = l.split("=", 1)
#                     res[key] = value.replace("\n", "")
#     except FileNotFoundError:
#         return {}

#     return res


# print(read_config("config.txt"))
