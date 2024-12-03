import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(filter_by_currency_fixture, filter_by_currency_true_dict_fixture):
    usd_transaction = list(filter_by_currency(filter_by_currency_fixture, "USD"))
    assert usd_transaction == filter_by_currency_true_dict_fixture


def test_filter_by_currency_error_1(filter_by_currency_is_not_fixture):
    with pytest.raises(ValueError) as exc_info:
        list(filter_by_currency(filter_by_currency_is_not_fixture, "USD"))
        assert str(exc_info.value) == "Нет необходимого ключа"


def test_filter_by_currency_error_2(filter_by_currency_wrong_currency_fixture):
    with pytest.raises(ValueError) as exc_info:
        list(filter_by_currency(filter_by_currency_wrong_currency_fixture, "USD"))
        assert str(exc_info.value) == "Нет верного пути"


def test_filter_by_currency_error_3(filter_by_currency_code_is_not_fixture):
    with pytest.raises(ValueError) as exc_info:
        list(filter_by_currency(filter_by_currency_code_is_not_fixture, "USD"))
        assert str(exc_info.value) == "Нет верного пути"


def test_transaction_descriptions(filter_by_currency_fixture, transaction_descriptions_result_fixture):
    descriptions_transaction = list(transaction_descriptions(filter_by_currency_fixture))
    assert descriptions_transaction == transaction_descriptions_result_fixture


def test_transaction_descriptions_error_1(transaction_descriptions_is_not_fixture):
    with pytest.raises(ValueError) as exc_info:
        list(transaction_descriptions(transaction_descriptions_is_not_fixture))
        assert str(exc_info.value) == "Нет необходимого ключа"


@pytest.mark.parametrize(
    "start, stop",
    [
        (1, 5),
        (1, 5),
        (1, 5),
        (1, 5),
        (1, 5),
    ],
)
def test_number_generator_correct_parm(start, stop):
    generator = card_number_generator(start, stop)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"
    assert next(generator) == "0000 0000 0000 0005"
