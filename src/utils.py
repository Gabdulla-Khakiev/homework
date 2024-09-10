import json
import logging
import os

from src.external_api import get_exchange_rate

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/utils.log")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

file_path = "data/operations.json"


def load_transactions(file_path):
    """Загружает данные о финансовых транзакциях из JSON-файла"""

    logger.info("Выполняем преобразование json файла в элемент python")

    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf8") as file:
            data = json.load(file)

        if isinstance(data, list):
            logger.info("Получили список словарей из json файла")
            return data
        else:
            logger.info("В файле нет списков")
            return []

    except (json.JSONDecodeError, FileNotFoundError) as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return []


def get_transaction_amount_in_rub(transaction):
    """Возвращает сумму транзакции в рублях."""
    amount = float(transaction["operationAmount"]["amount"])
    currency_code = transaction["operationAmount"]["currency"]["code"]

    if currency_code == "RUB":
        logger.info("Сумма вернулась без конвертации")
        return amount

    if currency_code in ["USD", "EUR"]:
        converted_amount = get_exchange_rate(amount, currency_code)
        if converted_amount:
            logger.info("Сумма вернулась после конвертации в рубли")
            return converted_amount
        else:
            logger.error(f"Произошла ошибка: {ValueError}")
            raise ValueError("Не удалось получить курс валюты.")

    # Для неподдерживаемых валют
    logger.error(f"Произошла ошибка: {ValueError}")
    raise ValueError(f"Неподдерживаемая валюта: {currency_code}")

