def filter_by_currency(transactions_list, currency):
    """Функция возвращает отсортированный список словарей по параметру 'currency'"""
    if not transactions_list:
        return []  # Вернуть пустой список, если входной список пуст

        # Фильтрация транзакций по валюте
    if "operationAmount" in transactions_list:
        filtered_transactions = [
            transaction for transaction in transactions_list
            if (
                    transaction.get("operationAmount") and
                    transaction["operationAmount"].get("currency") and
                    transaction["operationAmount"]["currency"].get("code") == currency
            )
        ]
    else:
        filtered_transactions = [
            transaction for transaction in transactions_list
            if transaction.get("currency_code") == currency
        ]

    return filtered_transactions


# Функция для генерации описаний транзакций


def transaction_descriptions(transactions):
    """Генератор, который возвращает описание каждой транзакции."""
    if not transactions:
        yield "Нет транзакций"
    else:
        for description_operation in transactions:
            yield description_operation.get("description")


def card_number_generator(start, stop):
    """Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX."""
    for number in range(start, stop + 1):
        card_number = f"{number:016d}"
        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_card_number
