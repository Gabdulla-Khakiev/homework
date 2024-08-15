import pytest
from src.masks import get_mask_card_number
from src.masks import get_mask_account


@pytest.mark.parametrize('card_number, expected', [
    ('2200255555555555', '2200 25** **** 5555'),
    ('1234567812345678', '1234 56** **** 5678'),
    ('123412341234', 'Это не номер карты!'),
    ('12341234123412341234', 'Это не номер карты!'),
    ('', 'Это не номер карты!'),
    (1234123412341234, 'Это не номер карты!')
])
def test_get_mask_card_number(valid_card_number, card_number, expected):
    """Тест для проверки функции для маскировки номера карты"""

    if card_number == valid_card_number:
        assert get_mask_card_number(valid_card_number) == '2200 25** **** 5555'

    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize('account_number, expected_mask', [
    ('73654108430135874305', '**4305'),
    ('', 'Это не номер счета'),
    (73654108430135874305, 'Это не номер счета'),
    ('736541084301358743051', 'Это не номер счета'),
    ('73654108430135874', 'Это не номер счета')
])
def test_get_mask_account(valid_account_number, account_number, expected_mask):
    """Тест для проверки функции для маскировки носера счета"""

    if account_number == valid_account_number:
        assert get_mask_account(valid_account_number) == '**4305'

    assert get_mask_account(account_number) == expected_mask
