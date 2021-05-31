import pytest
from leapyear import leapyear

ly = leapyear()

def test_div_by_4():
    assert ly.leapyear(2004) == True
    assert ly.leapyear(1996) == True
    assert ly.leapyear(1988) == True
    assert ly.leapyear(2016) == True

def test_div_by_100():
    assert ly.leapyear(2000) == False
    assert ly.leapyear(1900) == False
    assert ly.leapyear(1600) == False
    assert ly.leapyear(2800) == False

def test_div_by_400():
    assert ly.leapyear(2000) == True
    assert ly.leapyear(1600) == True
    assert ly.leapyear(1200) == True
    