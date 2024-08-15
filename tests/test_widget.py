import pytest
from src.widget import get_date
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
    ('Visa Classic 6831982476737', 'Ошибка ввода'),     # Слишком короткий номер карты
    ('Visa Gold 5999414228426353687', 'Ошибка ввода'),  # Слишком длинный номер карты
    ('Счет 73654108430135874', 'Ошибка ввода'),         # Слишком короткий номер счета
    ('Счет 73654108430135874305688', 'Ошибка ввода'),  # Слишком длинный номер счета
    ('', 'Ошибка ввода'),                              # Пустая строка
    ('73654108430135874', 'Ошибка ввода')              # Неправильный ввод
])
def test_mask_account_card(valid_card_number, valid_account_number, user_information, expected_result):

    if user_information == valid_card_number:
        assert mask_account_card(valid_card_number) == '2200 25** **** 5555'
    elif user_information == valid_account_number:
        assert mask_account_card(valid_account_number) == '**4305'

    assert mask_account_card(user_information) == expected_result


@pytest.mark.parametrize('date, expected_date', [
    ('2024-03-11T02:26:18.671407', '11.03.2024'),
    ('2019-07-03T18:35:29.512364', '03.07.2019')
])
def test_get_date(date, expected_date):
    assert get_date(date) == expected_date
