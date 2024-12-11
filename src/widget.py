from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: str) -> str:
    """функция ввода типа карты/счета"""
    if type_and_number == "":
        raise TypeError("Неверный тип строки")
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
        full_account = text_result + get_mask_account(digit_result)
        return full_account
    else:
        full_card = text_result + get_mask_card_number(digit_result)
        return full_card


first_num = "Maestro 7000792289606361"
print(mask_account_card(first_num))


def get_date(first_form_date: str) -> str:
    """функция ввода даты"""
    if first_form_date == "":
        raise TypeError("Неверный тип строки")
    worked_form_date = first_form_date[:10]

    changed_form_date = str(worked_form_date[-2:] + "." + worked_form_date[5:7] + "." + worked_form_date[:4])
    return changed_form_date


masked_date_num = "2024-03-11T02:26:18.671407"
print(get_date(masked_date_num))
