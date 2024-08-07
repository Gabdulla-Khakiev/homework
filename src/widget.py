from masks import get_mask_card_number
from masks import get_mask_account

def mask_account_card(user_information: str) -> str:
    words_list = user_information.split(" ")
    if words_list[-1].isdigit() and len(words_list[-1]) == 16:
        words_list[-1] = get_mask_card_number(words_list[-1])
    elif words_list[-1].isdigit():
        words_list[-1] = get_mask_account(words_list[-1])
    return " ".join(words_list)


if __name__ == "__main__":
    print(mask_account_card(input()))
