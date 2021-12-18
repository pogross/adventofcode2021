import pytest

from day01 import count_increasing


@pytest.mark.parametrize(
    "measurments, expected",
    [([1, 2, 3], 2), ([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 7)],
)
def test_task1(measurments, expected):
    actual = count_increasing(measurments)
    assert actual == expected


@pytest.mark.parametrize(
    "measurments, expected",
    [([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 5)],
)
def test_task2(measurments, expected):
    actual = count_increasing(measurments, 3)
    assert actual == expected
