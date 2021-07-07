""" Test sudoku using Hypothesis. """

from hypothesis import given
from hypothesis.strategies import lists, sampled_from, sets

SUDOKU_VALUES = list(range(1, 10))


def has_duplicates(row: list) -> bool:
    """Check row has no duplicates."""
    _row = [i for i in row if i != 0]
    return len(set(_row)) != len(_row)


@given(lists(sampled_from(SUDOKU_VALUES), min_size=10, max_size=10))
def test_has_duplicates(row):
    """Row has duplicates."""
    assert has_duplicates(row)


@given(sets(sampled_from(SUDOKU_VALUES), min_size=9, max_size=9))
def test_has_no_duplicates(row):
    """Row has no duplicates."""
    assert not has_duplicates(row)
