import random

import pytest
from testing_example import Calculator as c


@pytest.mark.parametrize('n, a, b, expected_result', [(0, 2, 2, 4),
                                                      (0, 1, 1, 2),
                                                      (0, 3, 3, 6)])
def test_sum(n, a, b, expected_result):
    assert c.sum(n, a, b) == expected_result


@pytest.mark.parametrize('n, a, b, expected_result', [(0, 2, 2, 4),
                                                      (0, 1, 1, 1),
                                                      (0, 3, 3, 9)])
def test_mult(n, a, b, expected_result):
    assert c.mult(n, a, b) == expected_result


@pytest.fixture()
def mean_a():
    return random.randint(1, 10)


@pytest.fixture()
def mean_b():
    return random.randint(1, 10)


def test_sum_fix(mean_a, mean_b):
    assert c.sum(0, mean_a, mean_b) == mean_a + mean_b


def test_mult_fix(mean_a, mean_b):
    assert c.mult(0, mean_a, mean_b) == mean_a * mean_b


if __name__ == "__main__":
    pytest.main()