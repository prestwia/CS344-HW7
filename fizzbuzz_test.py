import pytest
from fizzbuzz import fizzbuzz

fb = fizzbuzz()

def test_3():
    assert fb.fizzbuzz(3) == "Fizz"
    assert fb.fizzbuzz(12) == "Fizz"
    assert fb.fizzbuzz(36) == "Fizz"
    assert fb.fizzbuzz(93) == "Fizz"
    assert fb.fizzbuzz(4) == 4
    assert fb.fizzbuzz(28) == 28