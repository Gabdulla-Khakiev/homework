from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Функция возвращает замаскированный номер карты"""
    tmp_list = []
    counter = 0

    numbers_list = list(card_number)
    numbers_list[6:-4] = ["*", "*", "*", "*", "*", "*"]

    for i in numbers_list:
        tmp_list.append(i)
        counter += 1
        if counter % 4 == 0 and counter < 16:
            tmp_list.append(" ")
    masked_card_number = "".join(tmp_list)

    return masked_card_number


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Функция возвращает замаскированный номер счета"""

    last_numbers_string = account_number[-6:]
    last_numbers_list = list(last_numbers_string)
    last_numbers_list[:2] = ["*", "*"]
    masked_account_number = "".join(last_numbers_list)

    return masked_account_number
