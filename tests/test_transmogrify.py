import pytest
from transmogrify import transmogrify
def test_transmogrify_sum():
    assert transmogrify([1, 1], "odd", "sum") == 2

def test_transmogrify_multiply():
    assert transmogrify([3, 3], "odd", "multiply") == 9

def test_transmogrify_float():
    assert transmogrify([0.5, 3, "Afghanistan"], "float", "sum") == 3.5

def test_transmogrify_odd():
    assert transmogrify([3, 5, 2, "Malawi"], "odd", "sum") == 8

def test_transmogrify_even():
    assert transmogrify([2, 4, 5, "Haiti"], "even", "sum") == 6