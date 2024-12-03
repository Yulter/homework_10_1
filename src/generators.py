def filter_by_currency(transactions_list: list, valute: str):
    "функция нахождения кода"

    for transaction in transactions_list:

        if "currency" not in transaction["operationAmount"]:
            raise ValueError("Нет верного пути")

        if "code" not in transaction["operationAmount"]["currency"]:
            raise ValueError("Нет верного пути")

        if transaction["operationAmount"]["currency"]["code"] == "":
            raise ValueError("Нет необходимого ключа")

        if transaction["operationAmount"]["currency"]["code"] == valute:
            yield transaction


def transaction_descriptions(transactions_list: list):
    "функция выведения значения определенного ключа"
    for transaction in transactions_list:
        for k, v in transaction.items():

            if "description" not in transaction or k == "":
                raise ValueError("Нет необходимого ключа")

            if k == "description":
                yield v


def card_number_generator(start: int = 1, end: int = 20):
    """Функция генерирует номера карт в заданном диапазоне и выдаёт в корректном формате"""

    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Не верный тип данных входящих аргументов")

    if start > end:
        raise ValueError("Не верно заданы параметры start и stop, start должен быть меньше или равен stop")

    if len(str(start)) > 16 or len(str(end)) > 16:
        raise ValueError(
            "Слишком большое число передано в start/end, максимальная длина строки не должна превышать 16 символов"
        )

    while start <= end:
        formatted_number = f"{start:016}"
        formatted_number = " ".join([formatted_number[i : i + 4] for i in range(0, len(formatted_number), 4)])
        yield formatted_number
        start += 1
