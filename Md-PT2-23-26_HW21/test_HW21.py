import pytest
from practice_calculator import Calculator


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
def test_add(num1, num2, exp):
    calc = Calculator()
    assert calc.add(num1, num2) == exp


@pytest.mark.parametrize(
    "num1, num2, exp",
    [(5, 3, 2), (2, 5, -3), (3, 3, 0)],
    ids=[
        "test_subtract_positive_numbers",
        "test_subtract_negative_result",
        "test_subtract_same_numbers",
    ],
)
def test_subtract(num1, num2, exp):
    calc = Calculator()
    assert calc.subtract(num1, num2) == exp


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
def test_multiplay(num1, num2, exp):
    calc = Calculator()
    assert calc.multiply(num1, num2) == exp


@pytest.mark.parametrize(
    "num1, num2, exp",
    [(6, 3, 2), (-6, -3, 2)],
    ids=["test_divide_positive_numbers", "test_divide_negative_numbers"],
)
def test_divide(num1, num2, exp):
    calc = Calculator()
    assert calc.divide(num1, num2) == exp


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
def test_divide_result_is_float(num1, num2):
    calc = Calculator()
    assert isinstance(calc.divide(num1, num2), float)


@pytest.mark.parametrize(
    "num1, num2, exp",
    [(2, 3, 8), (2, 0, 1), (2, -1, 0.5)],
    ids=[
        "test_power_positive_exponent",
        "test_power_zero_exponent",
        "test_power_negative_exponent",
    ],
)
def test_power(num1, num2, exp):
    calc = Calculator()
    assert calc.power(num1, num2) == exp


@pytest.mark.parametrize(
    "num1, num2, exp",
    [(50, 10, 5), (50, 0, 0), (50, 100, 50)],
    ids=[
        "test_percentage_positive_value",
        "test_percentage_zero_percent",
        "test_percentage_hundred_percent",
    ],
)
def test_percentage(num1, num2, exp):
    calc = Calculator()
    assert calc.percentage(num1, num2) == exp


def test_history_empty_by_default():
    calc = Calculator()
    assert calc.get_history() == []


def test_history_after_add():
    calc = Calculator()
    calc.add(1, 2)
    assert calc.get_history() == ["1 + 2 = 3"]


def test_history_after_multiple_operations():
    calc = Calculator()
    calc.add(1, 2)
    calc.subtract(4, 3)
    calc.multiply(1, 2)
    assert len(calc.get_history()) == 3


def test_history_order():
    calc = Calculator()
    calc.add(1, 2)
    calc.subtract(4, 3)
    calc.multiply(1, 2)
    assert calc.get_history() == ["1 + 2 = 3", "4 - 3 = 1", "1 * 2 = 2"]


def test_clear_history():
    calc = Calculator()
    calc.add(1, 2)
    calc.subtract(4, 3)
    calc.multiply(1, 2)
    calc.clear_history()
    assert calc.get_history() == []


def test_get_history_returns_copy():
    calc = Calculator()
    calc.add(1, 2)
    history_copy = calc.get_history()
    history_copy.append("bla bla bla")
    assert calc.get_history() == ["1 + 2 = 3"]


def test_history_not_added_after_error():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(1, 0)
    assert calc.get_history() == []


def test_divide_by_zero_error_message():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError, match="Деление на ноль невозможно"):
        calc.divide(1, 0)


def test_percentage_negative_error_message():
    calc = Calculator()
    with pytest.raises(ValueError, match="Процент не может быть отрицательным"):
        calc.percentage(10, -1)


@pytest.mark.parametrize(
    "num1,num2",
    [("1", 2), (1, "2")],
    ids=["first_arg_string", "second_arg_string"],
)
def test_invalid_types_add(num1, num2):
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.add(num1, num2)


@pytest.mark.parametrize(
    "num1,num2",
    [("1", 2), (1, "2")],
    ids=["first_arg_string", "second_arg_string"],
)
def test_invalid_types_divide(num1, num2):
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.divide(num1, num2)
