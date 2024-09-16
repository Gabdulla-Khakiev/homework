import re


def search_operations(operations, search_string):
    """Возвращает список операций, у которых в описании есть строка поиска."""
    result = []
    for operation in operations:
        if re.search(search_string, operation.get('description', ''), re.IGNORECASE):
            result.append(operation)
    return result
