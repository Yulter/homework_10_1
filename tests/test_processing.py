import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "data, expected_state, expected_result",
    [
        (
            [
                {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
            "CANCELED",
            [
                {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        ([], "EXECUTED", []),
        ([], "CANCELED", []),
    ],
)
def test_filter_by_state(data, expected_state, expected_result):
    """тест на сортировку по значению"""
    assert filter_by_state(data, expected_state) == expected_result


@pytest.mark.parametrize(
    "date_1, order, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        ([], True, []),
        ([], False, []),
    ],
)
def test_sort_by_date(date_1, order, expected):
    """тест на сортировку по дате"""
    assert sort_by_date(date_1, order) == expected
