import logging
from typing import Union


logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/masks.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Функция возвращает замаскированный номер карты"""
    tmp_list = []
    counter = 0
    if isinstance(card_number, str):
        if len(card_number) == 16:
            logger.info("Применяется маска к номеру карты")

            numbers_list = list(card_number)
            numbers_list[6:-4] = ["*", "*", "*", "*", "*", "*"]

            for i in numbers_list:
                tmp_list.append(i)
                counter += 1
                if counter % 4 == 0 and counter < 16:
                    tmp_list.append(" ")
            masked_card_number = "".join(tmp_list)

            return masked_card_number
        else:
            logger.error(f"Произошла ошибка: Введен не номер карты")
            return "Это не номер карты!"
    else:
        logger.error(f"Произошла ошибка: Введен не номер карты")
        return "Это не номер карты!"


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Функция возвращает замаскированный номер счета"""

    if isinstance(account_number, str):
        if len(account_number) == 20:
            logger.info("Применяется маска к номеру счета")

            last_numbers_string = account_number[-6:]
            last_numbers_list = list(last_numbers_string)
            last_numbers_list[:2] = ["*", "*"]
            masked_account_number = "".join(last_numbers_list)

            return masked_account_number
        else:
            logger.error(f"Произошла ошибка: Введен не номер счета")
            return "Это не номер счета"
    else:
        logger.error(f"Произошла ошибка: Введен не номер счета")
        return "Это не номер счета"
