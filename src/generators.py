def filter_by_currency(transactions_list, currency):
    """Функция возвращает отсортированный список словарей по параметру 'currency' """
    if len(transactions_list) > 0:
        filtered_transactions = filter(
            lambda transactions_list_2:
            transactions_list.get("operationAmount").get("currency").get("code") == currency, transactions_list)
        return filtered_transactions
    else:
        return "Список пустой!"


def transaction_descriptions(transactions_list):
    """Генератор возвращает описание транзакции"""
    for transaction in transactions_list:
        yield transaction['description']


def card_number_generator(start, stop):
    """Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX."""
    for number in range(start, stop + 1):
        card_number = f"{number:016d}"
        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_card_number
