from src.search_and_categorize import search_operations, categorize_operations


def test_search_operations(transactions):
    # Поиск операций, связанных с "организации"
    result = search_operations(transactions, 'Перевод организации')
    assert len(result) == 2, "Ожидалось 2 операции с описанием, содержащим 'организации'"
    assert result[0]['description'] == "Перевод организации"
    assert result[1]['description'] == "Перевод организации"

    # Поиск операций с "карта"
    result = search_operations(transactions, 'Перевод с карты на карту')
    assert len(result) == 1, "Ожидалась 1 операция с описанием, содержащим 'карта'"
    assert result[0]['description'] == "Перевод с карты на карту"

    # Поиск по несуществующей строке
    result = search_operations(transactions, 'несуществующая строка')
    assert len(result) == 0, "Не должно быть операций с несуществующей строкой в описании"


# Тесты для функции категоризации операций
def test_categorize_operations(transactions):
    # Категории для теста
    categories = ['Перевод организации', 'Перевод со счета на счет', 'Перевод с карты на карту']

    # Ожидаемая категоризация
    result = categorize_operations(transactions, categories)

    assert result['Перевод организации'] == 2, "Ожидалось 2 операции для категории 'Перевод организации'"
    assert result['Перевод со счета на счет'] == 2, "Ожидалось 3 операции для категории 'Перевод со счета на счет'"
    assert result['Перевод с карты на карту'] == 1, "Ожидалась 1 операция для категории 'Перевод с карты на карту'"
