from typing import List


def filter_by_state(list_of_dict: List, state="EXECUTED"):
    """Функция возвращает список отсортированных словарей по параметру state"""
    for i in list_of_dict:
        if "state" in i:
            if state == "":
                state = "EXECUTED"
            return [item for item in list_of_dict if item.get("state") == state]
        else:
            return '"state" not found'


def sort_by_date(list_of_dict: List, reverse=True):
    """Функция возвращает отсртированный список по дате"""
    for i in list_of_dict:
        if "date" in i:
            return sorted(list_of_dict, key=lambda x: x.get("date", ""), reverse=reverse)
        else:
            return '"date" not found'
