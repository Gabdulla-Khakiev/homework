from typing import List


def filter_by_state(list_of_dict: List, state='EXECUTED') -> List:
    """Функция возвращает список отсортированных словарей по параметру state"""
    filtered_list = []
    for i in list_of_dict:
        if i['state'] == state:
            filtered_list.append(i)
    return filtered_list


def sort_by_date(list_of_dict_2: List, reverse=True):
    """Функция возвращает отсртированный список по дате"""
    return sorted(list_of_dict_2, key=lambda x: x['date'], reverse=reverse)


list_ = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

print(filter_by_state(list_))
