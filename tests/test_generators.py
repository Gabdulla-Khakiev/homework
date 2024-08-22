import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions):
    result = filter_by_currency(transactions, "USD")
    assert next(result) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(result) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(result) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }


def test_filter_by_currency_exceptions(transactions):
    result = filter_by_currency(transactions, "EUR")
    assert list(result) == []
    result = filter_by_currency([], "EUR")
    assert result == "Список пустой!"


@pytest.mark.parametrize(
    "index, expected",
    [
        (0, "Перевод организации"),
        (1, "Перевод со счета на счет"),
        (2, "Перевод со счета на счет"),
    ],
)
def test_transaction_descriptions(transactions, index, expected):
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions[index] == expected


def test_transaction_descriptions_exceptions():
    descriptions = transaction_descriptions([])
    assert list(descriptions) == ["Нет транзакций"]


@pytest.mark.parametrize(
    "start, stop, expected_numbers",
    [
        (1, 1, ["0000 0000 0000 0001"]),
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (1234567890123456, 1234567890123456, ["1234 5678 9012 3456"]),
        (9999999999999998, 9999999999999999, ["9999 9999 9999 9998", "9999 9999 9999 9999"]),
        (1000, 1000, ["0000 0000 0000 1000"]),
    ],
)
def test_card_number_generator(start, stop, expected_numbers):
    """Параметризованный тест генератора номеров карт."""
    generator = card_number_generator(start, stop)
    generated_numbers = list(generator)

    assert generated_numbers == expected_numbers
