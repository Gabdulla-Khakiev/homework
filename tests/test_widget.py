import pytest
# from src.widget import get_date
from src.widget import mask_account_card


@pytest.mark.parametrize('user_information, expected_result', [
    ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
    ('Счет 64686473678894779589', 'Счет **9589'),
    ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
    ('Счет 35383033474447895560', 'Счет **5560'),
    ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
    ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
    ('Visa Gold 5999414228426353', 'Visa Gold 5999 41** **** 6353'),
    ('Счет 73654108430135874305', 'Счет **4305'),
    (1234123412341234, 'Ошибка ввода'),
    ('Visa Classic 6831982476737', 'Ошибка ввода'),
    ('Visa Gold 5999414228426353687', 'Ошибка ввода'),
    ('Счет 73654108430135874', 'Ошибка ввода'),
    ('Счет 73654108430135874305688', 'Ошибка ввода'),
    ('', 'Ошибка ввода'),
    ('73654108430135874', 'Ошибка ввода')
])
def test_mask_account_card(user_information, expected_result):
    assert mask_account_card(user_information) == expected_result


# @pytest.mark.parametrize()
# def test_get_date():
#     pass
