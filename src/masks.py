from typing import Union


def get_mask_card_number(num_of_card: Union[int, str]) -> str:
    """функция ввода номера карты"""
    num_of_card = str(num_of_card)
    # превращаем в строку
    masked_num_of_card = num_of_card[-16:-10] + "******" + num_of_card[-4:]
    result = " ".join(
        [masked_num_of_card[-16:-12], masked_num_of_card[-12:-8], masked_num_of_card[-8:-4], masked_num_of_card[-4:]]
    )

    return result


def get_mask_account(account_number: Union[int, str]) -> str:
    """функция ввода номера счета"""
    account_number = str(account_number)
    # превращаем в строку
    masked_acc_num = account_number[-20:-6] + "**" + account_number[-4:]
    result_1 = "".join([masked_acc_num[-6:-4], masked_acc_num[-4:]])

    return result_1
