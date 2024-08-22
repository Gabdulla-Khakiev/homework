import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, expected_list",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        ("NOT_FOUND", []),
        (
            "",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
    ],
)
def test_filter_by_state(list_for_tests, state, expected_list):
    """Тест для проверки функции которая фильтрует список словарей по параметру state"""
    assert filter_by_state(list_for_tests, state) == expected_list


@pytest.mark.parametrize(
    "state, expected",
    [
        ("EXECUTED", '"state" not found'),
        ("CANCELED", '"state" not found'),
        ("", '"state" not found'),
        ("NOT_FOUND", '"state" not found'),
    ],
)
def test_empty_state(empty_state_list_for_tests, state, expected):
    """Тест для проверки функции которая фильтрует список словарей по параметру state,
    если список не имеет параметра state или список пустой"""
    assert filter_by_state(empty_state_list_for_tests, state) == expected


@pytest.mark.parametrize(
    "reverse, expected",
    [
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
        (
            bool,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
    ],
)
def test_sort_by_date(list_for_tests, empty_state_list_for_tests, reverse, expected):
    """Тест для проверки функции которая сортирует список словарей по параметру date"""
    assert sort_by_date(list_for_tests, reverse) == expected


@pytest.mark.parametrize(
    "reverse, expected",
    [
        (
            True,
            [
                {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "date": "2018-06-30T02:08:58.425572"},
                {"id": 615064591, "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": 594226727, "date": "2018-06-30T02:08:58.425572"},
                {"id": 615064591, "date": "2018-06-30T02:08:58.425572"},
                {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date_same_dates(empty_state_list_for_tests, reverse, expected):
    """Тест для проверки функции которая сортирует список словарей по параметру date, если даты одинаковые"""
    assert sort_by_date(empty_state_list_for_tests, reverse) == expected


@pytest.mark.parametrize("reverse, expected", [(True, '"date" not found'), (False, '"date" not found')])
def test_sort_by_date_empty_date(empty_date_list_for_tests, reverse, expected):
    """Тест для проверки функции которая сортирует список словарей по параметру date, если даты нет или список пуст"""
    assert sort_by_date(empty_date_list_for_tests, reverse) == expected
