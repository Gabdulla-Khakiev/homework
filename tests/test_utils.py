import pytest
import json
from unittest.mock import patch, mock_open
from src.utils import load_transactions, get_transaction_amount_in_rub


@pytest.fixture()
@patch("builtins.open", new_callable=mock_open,
       read_data='[{"id": 1, "operationAmount": {"amount": "1000", "currency": {"code": "USD"}}}]')
def test_load_transactions_valid(mock_file):
    """Тест для проверки корректной загрузки транзакций из файла."""
    transactions = load_transactions("data/operations.json")
    assert len(transactions) == 1
    assert transactions[0]["id"] == 1


@patch("builtins.open", new_callable=mock_open)
def test_load_transactions_invalid_json(mock_file):
    """Тест для проверки обработки ошибки JSONDecodeError."""
    mock_file.return_value.read.side_effect = json.JSONDecodeError("Expecting value", "", 0)
    transactions = load_transactions("data/operations.json")
    assert transactions == []


@patch("os.path.exists", return_value=False)
def test_load_transactions_file_not_found(mock_exists):
    """Тест для проверки случая, когда файл не найден."""
    transactions = load_transactions("data/operations.json")
    assert transactions == []


# Тесты для функции get_transaction_amount_in_rub
@patch("src.utils.get_exchange_rate", return_value=75000.0)
def test_get_transaction_amount_in_rub_usd(mock_get_exchange_rate):
    """Тест для проверки конвертации из USD в RUB."""
    transaction = {
        "operationAmount": {"amount": "1000", "currency": {"code": "USD"}}
    }
    amount_in_rub = get_transaction_amount_in_rub(transaction)
    mock_get_exchange_rate.assert_called_once_with(1000.0, "USD")
    assert amount_in_rub == 75000.0


@patch("src.utils.get_exchange_rate", return_value=None)
def test_get_transaction_amount_in_rub_api_error(mock_get_exchange_rate):
    """Тест для проверки обработки ошибки API при конвертации валюты."""
    transaction = {
        "operationAmount": {"amount": "1000", "currency": {"code": "USD"}}
    }
    with pytest.raises(ValueError, match="Не удалось получить курс валюты."):
        get_transaction_amount_in_rub(transaction)


def test_get_transaction_amount_in_rub_rub():
    """Тест для проверки случая, когда валюта уже в рублях."""
    transaction = {
        "operationAmount": {"amount": "1000", "currency": {"code": "RUB"}}
    }
    amount_in_rub = get_transaction_amount_in_rub(transaction)
    assert amount_in_rub == 1000.0


def test_get_transaction_amount_in_rub_unsupported_currency():
    """Тест для проверки обработки неподдерживаемой валюты."""
    transaction = {
        "operationAmount": {"amount": "1000", "currency": {"code": "JPY"}}
    }
    with pytest.raises(ValueError, match="Неподдерживаемая валюта: JPY"):
        get_transaction_amount_in_rub(transaction)
