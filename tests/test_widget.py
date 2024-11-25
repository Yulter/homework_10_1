import pytest
from src.masks import get_mask_card_number, get_mask_account
from src.widget import get_date, mask_account_card

@pytest.mark.parametrize("some_number, some_correct_number", [('Maestro 7000792289606361', 'Maestro 7000 79** **** 6361'),
                                                              ('Счет 35383033474447895560', 'Счет **5560')])



def test_mask_account_card(some_number, some_correct_number):
    if some_number == 16:
        assert get_mask_card_number(some_number) == some_correct_number
    if some_number == 20:
        assert mask_account_card(some_number) == some_correct_number

def test_mask_account_card_type():
    with pytest.raises(TypeError) as exc_info:
        mask_account_card('')
    assert str(exc_info.value) == "Неверный тип строки"

def test_mask_account_card_len():
    with pytest.raises(ValueError) as exc_info:
        mask_account_card("1h1hhh")
    assert str(exc_info.value) == "Неверная длина строки"


@pytest.mark.parametrize("data_test, correct_data", [('2024-03-11T02:26:18.671407', '11.03.2024'),
                                                     ('2025-03-11T02:26:18.671407', '11.03.2025')])

def test_get_date(data_test, correct_data):
    assert get_date(data_test) == correct_data

def test_get_date():
    with pytest.raises(TypeError) as exc_info:
        get_date("")
    assert str(exc_info.value) == "Неверный тип строки"


