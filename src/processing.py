data = [
    {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
]


def filter_by_state(list: data, state="EXECUTED") -> list:
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
