import re


def search_operations(operations, search_string):
    """Возвращает список операций, у которых в описании есть строка поиска."""
    result = []
    for operation in operations:
        if re.search(search_string, operation.get('description', ''), re.IGNORECASE):
            result.append(operation)
    return result


def categorize_operations(operations, categories):
    """Возвращает словарь с количеством операций в каждой категории."""
    category_count = {category: 0 for category in categories}

    for operation in operations:
        description = operation.get('description', '').lower()
        for category in categories:
            if category.lower() in description:
                category_count[category] += 1

    return category_count
