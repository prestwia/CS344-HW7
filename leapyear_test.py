import pytest
from leapyear import leapyear

ly = leapyear()

def test_3():
    assert ly.leapyear(2004) == True
    assert ly.leapyear(1996) == True
    assert ly.leapyear(1988) == True
    assert ly.leapyear(2016) == True
    