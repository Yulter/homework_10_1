import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("card_number, correct_number", [('7000792289606361', '7000 79** **** 6361'),
                                                         ('9000792289606361', '9000 79** **** 6361')])
def test_get_mask_card_number(card_number, correct_number):
    assert get_mask_card_number(card_number) == correct_number

def test_len_card_number():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number('35383033474447895560')
    assert str(exc_info.value) == "Неверная длина строки"


def test_type_card_number():
    with pytest.raises(TypeError) as exc_info:
        get_mask_card_number('1nn1n')

        get_mask_card_number('')
    assert str(exc_info.value) == "Неверный тип строки"

@pytest.mark.parametrize("num_of_account, correct_account_number", [('64686473678894779589', '**9589'),
                                                                    ('35383033474447895560', '**5560')])

def test_get_mask_account(num_of_account, correct_account_number):
    assert get_mask_account(num_of_account) == correct_account_number

def test_len_account_number():
    with pytest.raises(ValueError) as exc_info:
        get_mask_account('3538303347444789556099')
    assert str(exc_info.value) == "Неверная длина строки"

def test_type_account_number():
    with pytest.raises(TypeError) as exc_info:
        get_mask_account('rg1g1')
        get_mask_account('')
    assert str(exc_info.value) == "Неверный тип строки"






