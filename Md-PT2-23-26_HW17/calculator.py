import argparse


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    if num2 == 0:
        return "Лучше не надо делить на 0"
    return num1 / num2


def pow_func(num1, num2):
    return num1**num2


def main():
    parser = argparse.ArgumentParser(description="HW_17")

    parser.add_argument("-a", type=float, required=True, help="Первое число")
    parser.add_argument("-b", type=float, required=True, help="Второе число")
    parser.add_argument(
        "-op",
        type=str,
        required=True,
        choices=["add", "sub", "mul", "div", "pow"],
        help="Операция: add (+), sub (-), mul (*), div (/), pow (**)",
    )

    args = parser.parse_args()
    num1 = args.a
    num2 = args.b

    if args.op == "add":
        print("Вы выбрали сумму")
        print(f"Результат: {num1} + {num2} = {add(num1, num2)}")

    elif args.op == "sub":
        print("Вы выбрали вычитание")
        print(f"Результат: {num1} - {num2} = {sub(num1, num2)}")

    elif args.op == "div":
        print("Вы выбрали деление")
        res = div(num1, num2)
        if res == "Лучше не надо делить на 0":
            print(res)
        else:
            print(f"Результат: {num1} / {num2} = {res}")

    elif args.op == "mul":
        print("Вы выбрали умножение")
        print(f"Результат: {num1} * {num2} = {mul(num1, num2)}")

    elif args.op == "pow":
        print("Вы выбрали возведение в степень")
        print(
            f"Результат возведение числа {num1} в степень {num2} равна {pow_func(num1, num2)}"
        )


if __name__ == "__main__":
    main()
