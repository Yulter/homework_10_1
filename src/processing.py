from typing import Dict, List

data = [
    {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
]


def filter_by_state(data: List[Dict[str, str]], state="EXECUTED") -> List[Dict[str, str]]:
    """функция получения списка словарей"""
    data_state = []
    for dictionary in data:
        if dictionary["state"] == "executed".upper():
            data_state.append(dictionary)
        else:
            continue

    return data_state


full_res_dic = filter_by_state(data)
print(full_res_dic)


data_1 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def sort_by_date(data_1: List[Dict[str, str]], order=True) -> List[Dict[str, str]]:
    """функция сортировки по дате"""
    sorted_user_date = sorted(data_1, key=lambda p: p["date"], reverse=order)
    return sorted_user_date


sorted_user_date_fin = sort_by_date(data_1)
print(sorted_user_date_fin)
