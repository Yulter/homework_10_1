from typing import Any, Dict, List

data = [
    {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
]


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """функция получения списка словарей"""
    data_state = []
    for dictionary in data:
        if dictionary["state"] == "executed".upper():
            data_state.append(dictionary)
        else:
            continue

    return data_state


full_result_dict = filter_by_state(data)
print(full_result_dict)


data_1 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def sort_by_date(data_1: List[Dict[str, Any]], order: bool = True) -> List[Dict[str, Any]]:
    """функция сортировки по дате"""
    sorted_user_date = sorted(data_1, key=lambda p: p["date"], reverse=order)
    return sorted_user_date


sorted_user_date_final = sort_by_date(data_1)
print(sorted_user_date_final)
