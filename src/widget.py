from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: str) -> str:
    """функция ввода типа карты/счета"""
    text_result = ""
    digit_result = ""
    digit_count = 0
    for num in type_and_number:
        if num.isalpha():
            text_result += num
        elif num.isdigit():
            digit_result += num
            digit_count += 1
    if digit_count > 16:
        full_acc = text_result + get_mask_account(digit_result)
        return full_acc
    else:
        full_card = text_result + get_mask_card_number(digit_result)
        return full_card


first_num = input()
print(mask_account_card(first_num))


def get_date(first_form_date: str) -> str:
    """функция ввода даты"""
    worked_form_date = first_form_date[:10]
    changed_form_date = str(worked_form_date[-2:] + "." + worked_form_date[5:7] + "." + worked_form_date[:4])
    return changed_form_date


date = input()
masked_date_num = get_date(date)
print(masked_date_num)
