from typing import List


def filter_by_state(list_of_dict: List, state='EXECUTED'):
    """Функция возвращает список отсортированных словарей по параметру state"""
    if 'state' in list_of_dict:
        if state == '':
            state = 'EXECUTED'
        return [item for item in list_of_dict if item['state'] == state]
    else:
        return '"state" not found'


def sort_by_date(list_of_dict: List, reverse=True):
    """Функция возвращает отсртированный список по дате"""
    if 'date' in list_of_dict:
        return sorted(list_of_dict, key=lambda x: x['date'], reverse=reverse)
    else:
        return '"date" not found'


if __name__ == '__main__':
    print(sort_by_date([
        {'id': 41428829, 'state': 'EXECUTED'},
        {'id': 939719570, 'state': 'EXECUTED'},
        {'id': 594226727, 'state': 'CANCELED'},
        {'id': 615064591, 'state': 'CANCELED'}
    ], ))
