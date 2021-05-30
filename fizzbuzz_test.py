import pytest
from fizzbuzz import fizzbuzz

fb = fizzbuzz()

def test_3():
    assert fb.fizzbuzz(3) == "Fizz"
    assert fb.fizzbuzz(12) == "Fizz"
    assert fb.fizzbuzz(36) == "Fizz"
    assert fb.fizzbuzz(93) == "Fizz"

def test_5():
    assert fb.fizzbuzz(5) == "Buzz"
    assert fb.fizzbuzz(35) == "Buzz"
    assert fb.fizzbuzz(50) == "Buzz"
    assert fb.fizzbuzz(95) == "Buzz"

def test_3_5():
    assert fb.fizzbuzz(15) == "FizzBuzz"
    assert fb.fizzbuzz(30) == "FizzBuzz"
    assert fb.fizzbuzz(45) == "FizzBuzz"
    assert fb.fizzbuzz(60) == "FizzBuzz"
    assert fb.fizzbuzz(90) == "FizzBuzz"
    