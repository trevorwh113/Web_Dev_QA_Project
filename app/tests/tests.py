import pytest
import utility

#test



#Unit tests for validate_string() and validate_int()
def test_valstring1():
    assert(utility.valid_string("")) == False 

def test_valstring2():
    assert(utility.valid_string("   ")) == False 

def test_valstring3():
    assert(utility.valid_string("hawk tuah")) == True

def test_valint1():
    assert(utility.valid_int()) == False

def test_valint1():
    assert(utility.valid_int("yummers")) == False

def test_valint2():
    assert(utility.valid_int(-3215314124)) == False

def test_valint3():
    assert(utility.valid_int(0)) == True

def test_valint4():
    assert(utility.valid_int(24)) == True
