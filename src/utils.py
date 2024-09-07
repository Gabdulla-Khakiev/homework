import json
import os
from src.external_api import get_exchange_rate


file_path = 'data/operations.json'


def load_transactions(file_path):
    """Загружает данные о финансовых транзакциях из JSON-файла"""

    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data
        else:
            return []

    except (json.JSONDecodeError, FileNotFoundError):
        return []


def get_transaction_amount_in_rub(transaction):
    """Возвращает сумму транзакции в рублях."""
    amount = float(transaction['operationAmount']['amount'])
    currency_code = transaction['operationAmount']['currency']['code']

    if currency_code == 'RUB':
        return amount

    if currency_code in ['USD', 'EUR']:
        converted_amount = get_exchange_rate(amount, currency_code)
        if converted_amount:
            return converted_amount
        else:
            raise ValueError("Не удалось получить курс валюты.")

    # Для неподдерживаемых валют
    raise ValueError(f"Неподдерживаемая валюта: {currency_code}")
