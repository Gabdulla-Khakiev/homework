from typing import List


def filter_by_state(list_of_dict: List, state='EXECUTED') -> List:
    """Функция возвращает список отсортированных словарей по параметру state"""
    filtered_list = []
    for i in list_of_dict:
        if i['state'] == state:
            filtered_list.append(i)
    return filtered_list


def sort_by_date(list_of_dict_2: List, reverse=True) -> List:
    """Функция возвращает отсртированный список по дате"""
    return sorted(list_of_dict_2, key=lambda x: x['date'], reverse=reverse)
