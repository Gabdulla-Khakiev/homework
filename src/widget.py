from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_information: str) -> str:
    """Функция маскирует номер счета и карты"""
    if isinstance(user_information, str):
        words_list = user_information.split(" ")

        if words_list[-1].isdigit() and len(words_list[-1]) == 16:
            words_list[-1] = get_mask_card_number(words_list[-1])
        elif words_list[-1].isdigit() and len(words_list[-1]) == 20:
            words_list[-1] = get_mask_account(words_list[-1])
        else:
            return "Ошибка ввода"

        return " ".join(words_list)
    else:
        return "Ошибка ввода"


def get_date(date: str) -> str:
    """Функция меняет формат написания даты."""
    try:
        # Попробуем обработать дату в формате '2023-09-05T11:30:32Z'
        if date.endswith("Z"):
            date = date[:-1]  # Убираем 'Z'
            dt = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
        else:
            dt = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")

        # Преобразуем в нужный формат
        modified_date = dt.strftime("%d.%m.%Y")
        return modified_date
    except ValueError:
        raise ValueError("Invalid datetime format")
