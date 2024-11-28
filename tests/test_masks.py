import pytest
from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_number_fixture):
    assert get_mask_card_number(card_number_fixture) == "7000 79** **** 6361"


def test_len_card_number():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("35383033474447895560")
    assert str(exc_info.value) == "Неверная длина строки"


def test_type_card_number():
    with pytest.raises(TypeError) as exc_info:
        get_mask_card_number("1nn1n")

        get_mask_card_number("")
    assert str(exc_info.value) == "Неверный тип строки"


def test_get_mask_account(num_of_account_fixture):
    assert get_mask_account(num_of_account_fixture) == "**9589"


def test_len_account_number():
    with pytest.raises(ValueError) as exc_info:
        get_mask_account("3538303347444789556099")
    assert str(exc_info.value) == "Неверная длина строки"


def test_type_account_number():
    with pytest.raises(TypeError) as exc_info:
        get_mask_account("rg1g1")
        get_mask_account("")
    assert str(exc_info.value) == "Неверный тип строки"
