import pytest
from functions.addition import add
from functions.multiplication import multiply


def test_add():
    assert add(3, 7) == 10
    assert type(add(12, '30')) is int
    assert add('23', 'foo') == 'invalid input'


def test_multiply():
    with pytest.raises(Exception):
        assert multiply(3, 7) == 21
        assert type(multiply(12, '30')) is int
        assert multiply('23', 'foo') == 'invalid input'
