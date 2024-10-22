"""
Unit tests the validation functions for string and int
inputs in utility.py.
"""
import pytest
import utility

# Unit tests for validate_string() // Casts to non-empty string
def test_valstring0():
    assert utility.valid_string() == False 

def test_valstring0():
    assert utility.valid_string("") == False 

def test_valstring2():
    assert utility.valid_string("   ") == False 

def test_valstring3():
    assert utility.valid_string("hawk tuah") == True

def test_valstring4():
    assert utility.valid_string(0) == True

def test_valstring5():
    assert utility.valid_string(-1.5) == True

def test_valstring6():
    assert utility.valid_string([]) == True


# Unit tests for validate_int() // Casts to non-negative int
def test_valint0():
    assert utility.valid_int("") == False

def test_valint1():
    assert utility.valid_int("yummers") == False

def test_valint2():
    assert utility.valid_int([]) == False

def test_valint3():
    assert utility.valid_int(-1) == False

def test_valint4():
    assert utility.valid_int(1) == True

def test_valint5():
    assert utility.valid_int(0) == True

def test_valint6():
    assert utility.valid_int(1.5) == True
