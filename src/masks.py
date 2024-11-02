from typing import Union


def get_mask_card_number(num_of_card: Union[int, str]) -> str:
    """функция ввода номера карты"""
    num_of_card = str(num_of_card)
    # превращаем в строку
    masked_num_of_card = num_of_card[:6] + "******" + num_of_card[12:]
    result = " ".join(
        [masked_num_of_card[0:4], masked_num_of_card[4:8], masked_num_of_card[8:12], masked_num_of_card[12:16]]
    )

    return result


card_num = input()
masked_card_num = get_mask_card_number(card_num)
print(masked_card_num)


def get_mask_account(account_number: Union[int, str]) -> str:
    """функция ввода номера счета"""
    account_number = str(account_number)
    # превращаем в строку
    masked_acc_num = account_number[:14] + "**" + account_number[-4:]
    result_1 = "".join([masked_acc_num[-6:-4], masked_acc_num[-4:]])

    return result_1


acc_num = input()
make_acc_num = get_mask_account(acc_num)
print(make_acc_num)
