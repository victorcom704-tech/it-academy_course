import pytest


@pytest.mark.parametrize(
    "num1,num2,exp",
    [(1, 2, 3), (3, 0, 3), (-1, -2, -3), (2.5, 1.5, 4.0)],
    ids=[
        "test_add_positive_numbers",
        "test_add_with_zero",
        "test_add_negative_numbers",
        "test_add_float_numbers",
    ],
)
def test_add(calculator, num1, num2, exp):
    assert calculator.add(num1, num2) == exp


@pytest.mark.parametrize(
    "num1, num2, exp",
    [(5, 3, 2), (2, 5, -3), (3, 3, 0)],
    ids=[
        "test_subtract_positive_numbers",
        "test_subtract_negative_result",
        "test_subtract_same_numbers",
    ],
)
def test_subtract(calculator, num1, num2, exp):
    assert calculator.subtract(num1, num2) == exp


@pytest.mark.parametrize(
    "num1, num2, exp",
    [(2, 3, 6), (2, 0, 0), (-2, -3, 6), (1.5, 4.0, 6.0)],
    ids=[
        "test_multiply_positive_numbers",
        "test_multiply_by_zero",
        "test_multiply_negative_numbers",
        "test_multiply_float_numbers ",
    ],
)
def test_multiplay(calculator, num1, num2, exp):
    assert calculator.multiply(num1, num2) == exp


@pytest.mark.parametrize(
    "num1, num2, exp",
    [(6, 3, 2), (-6, -3, 2)],
    ids=["test_divide_positive_numbers", "test_divide_negative_numbers"],
)
def test_divide(calculator, num1, num2, exp):
    assert calculator.divide(num1, num2) == exp


@pytest.mark.parametrize(
    "num1, num2",
    [
        (10, 2),
        (6, 4),
    ],
    ids=[
        "test_divide_result_is_float",
        "test_divide_result_is_float",
    ],
)
def test_divide_result_is_float(calculator, num1, num2):
    assert isinstance(calculator.divide(num1, num2), float)


@pytest.mark.parametrize(
    "num1, num2, exp",
    [(2, 3, 8), (2, 0, 1), (2, -1, 0.5)],
    ids=[
        "test_power_positive_exponent",
        "test_power_zero_exponent",
        "test_power_negative_exponent",
    ],
)
def test_power(calculator, num1, num2, exp):
    assert calculator.power(num1, num2) == exp


@pytest.mark.parametrize(
    "num1, num2, exp",
    [(50, 10, 5), (50, 0, 0), (50, 100, 50)],
    ids=[
        "test_percentage_positive_value",
        "test_percentage_zero_percent",
        "test_percentage_hundred_percent",
    ],
)
def test_percentage(calculator, num1, num2, exp):
    assert calculator.percentage(num1, num2) == exp


def test_history_empty_by_default(calculator):
    assert calculator.get_history() == []


def test_history_after_add(calculator):
    calculator.add(1, 2)
    assert calculator.get_history() == ["1 + 2 = 3"]


def test_history_after_multiple_operations(calculator):
    calculator.add(1, 2)
    calculator.subtract(4, 3)
    calculator.multiply(1, 2)
    assert len(calculator.get_history()) == 3


def test_history_order(calculator):
    calculator.add(1, 2)
    calculator.subtract(4, 3)
    calculator.multiply(1, 2)
    assert calculator.get_history() == ["1 + 2 = 3", "4 - 3 = 1", "1 * 2 = 2"]


def test_clear_history(calculator):
    calculator.add(1, 2)
    calculator.subtract(4, 3)
    calculator.multiply(1, 2)
    calculator.clear_history()
    assert calculator.get_history() == []


def test_get_history_returns_copy(calculator):
    calculator.add(1, 2)
    history_copy = calculator.get_history()
    history_copy.append("bla bla bla")
    assert calculator.get_history() == ["1 + 2 = 3"]


def test_history_not_added_after_error(calculator):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(1, 0)
    assert calculator.get_history() == []


def test_divide_by_zero_error_message(calculator):
    with pytest.raises(ZeroDivisionError, match="Деление на ноль невозможно"):
        calculator.divide(1, 0)


def test_percentage_negative_error_message(calculator):
    with pytest.raises(ValueError, match="Процент не может быть отрицательным"):
        calculator.percentage(10, -1)


@pytest.mark.parametrize(
    "num1,num2",
    [("1", 2), (1, "2")],
    ids=["first_arg_string", "second_arg_string"],
)
def test_invalid_types_add(calculator, num1, num2):
    with pytest.raises(TypeError):
        calculator.add(num1, num2)


@pytest.mark.parametrize(
    "num1,num2",
    [("1", 2), (1, "2")],
    ids=["first_arg_string", "second_arg_string"],
)
def test_invalid_types_divide(calculator, num1, num2):
    with pytest.raises(TypeError):
        calculator.divide(num1, num2)
