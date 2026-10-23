import logging

# 1
# logging.basicConfig(filename="app_session.log", filemode="w", level=logging.INFO)

# logging.debug("It's DEBUG")
# logging.info("It's INFO")
# logging.critical("It's CRITICAL")


# 2
# def repeat_string(text, count):
#     assert isinstance(text, str), "Аргумент должнен быть строкой"
#     assert isinstance(count, int), "Аргумент должен быть числом"
#     return text * count


# print(repeat_string("HW_16", 3))
# print(repeat_string(3, 3))
# print(repeat_string("A", "A"))

# 3
# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)

# combined_handler = logging.FileHandler("combined.log")
# combined_handler.setLevel(logging.INFO)

# error_handler = logging.FileHandler("crit_errors.log")
# error_handler.setLevel(logging.ERROR)

# logger.addHandler(combined_handler)
# logger.addHandler(error_handler)

# logger.info("INFO")
# logger.warning("WARNING")
# logger.error("ERROR")
# logger.critical("CRITICAL")

# 4
# logger = logging.getLogger()
# logger.setLevel(logging.ERROR)

# user_data = {"name": "Alice"}

# try:
#     age = user_data["age"]
# except KeyError:
#     logger.exception("Возраст не указан, прикинь на глаз")

# 5
# logging.basicConfig(level=logging.INFO)


# def process_payment(amount):
#     try:
#         assert amount > 0, "Введите сумму больше нуля"
#     except ArithmeticError:
#         logging.exception("Платёж не выполнен")
#         return False
#     logging.info(f"Платеж на сумму {amount} проведен успешно")
#     return True


# process_payment(50)
# process_payment(0)
