import pytest
from leapyear import leapyear

ly = leapyear()

def div_by_4():
    assert ly.leapyear(1996) == True
    assert ly.leapyear(2004) == True
    assert ly.leapyear(1998) == True
    assert ly.leapyear(1904) == True