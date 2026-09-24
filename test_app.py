import pytest
from app import sum_list, count_negatives

# 4 Input test cases for sum_list
@pytest.mark.parametrize("numbers, expected", [
    ([], 0),
    ([1, 2, 3], 6),
    ([-1, -2, -3], -6),
    ([1.5, 2.5], 4.0)
])
def test_sum_list(numbers, expected):
    assert sum_list(numbers) == expected


# 3 Valid cases + 1 Defective case with a wrong expected value (total 4 cases)
@pytest.mark.parametrize("numbers, expected", [
    ([], 0),
    ([1, 2, 3], 0),
    ([-1, 2, -3], 2),
    ([-5, -10], 99)  # <--- INTENTIONAL ERROR: Expected 99 instead of 2
])
def test_count_negatives(numbers, expected):
    assert count_negatives(numbers) == expected
