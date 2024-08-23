import pytest
from src.decorators import log


@log(filename=None)
def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def test_log(result_for_log, capsys):
    """Тест для проверки корректной работы декоратора 'log' """

    assert get_nod(2, 100000000) == 2
    assert capsys.readouterr().out.strip() == result_for_log.strip()


def test_log_exception(result_for_log_exception, capsys):
    """Тест для проверки декоратора 'log' в случае ошибки"""
    with pytest.raises(TypeError):
        get_nod('2', 100000000)

    assert capsys.readouterr().out.strip() == result_for_log_exception.strip()
