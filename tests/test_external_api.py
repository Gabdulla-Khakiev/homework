import os
from unittest.mock import patch

import requests

from src.external_api import get_exchange_rate


# Тест для успешного получения курса валюты
@patch("src.external_api.requests.get")
def test_get_exchange_rate_success(mock_get):
    # Определяем, что должен вернуть mock-запрос
    mock_response = {"success": True, "query": {"from": "USD", "to": "RUB", "amount": 100}, "result": 7500.00}

    # Настройка mock-ответа для requests.get
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    # Тестируем функцию
    result = get_exchange_rate(100, "USD", "RUB")

    assert result == 7500.00
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100",
        headers={"apikey": os.getenv("EXCHANGES_API")},
    )


# Тест для обработки ошибки RequestException
@patch("src.external_api.requests.get")
def test_get_exchange_rate_failure(mock_get):
    # Настройка mock-ответа для requests.get
    mock_get.side_effect = requests.RequestException("Ошибка сети")

    # Тестируем функцию
    result = get_exchange_rate(100, "USD", "RUB")

    assert result is None
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100",
        headers={"apikey": os.getenv("EXCHANGES_API")},
    )
