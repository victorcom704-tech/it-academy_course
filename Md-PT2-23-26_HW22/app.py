import time
import random


# 2.1
def process_files():
    print("Обработка файлов...")
    time.sleep(3)
    print("Готово!")
    return "processed"


# 2.2
def read_config(filename):
    with open(filename, "r") as f:
        return f.read().strip()


# 2.3
def generate_password(length=8):
    chars = "abc123"
    return "".join(random.choice(chars) for i in range(length))
