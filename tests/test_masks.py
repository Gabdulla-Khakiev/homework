import pytest
from src.masks import get_mask_card_number


@pytest.mark.parametrize('card_number, expected', [
    ('2200255555555555', '2200 25** **** 5555'),
    ('1234567812345678', '1234 56** **** 5678'),
    ('123412341234', 'Это не номер карты!'),
    ('12341234123412341234', 'Это не номер карты!'),
    ('', 'Это не номер карты!'),
    (1234123412341234, 'Это не номер карты!')
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected
