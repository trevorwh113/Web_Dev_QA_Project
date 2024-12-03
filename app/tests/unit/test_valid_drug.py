"""
Unit tests the validation function for drug
inputs in utility.py.
"""
import utility
import pytest

# Unit tests for validate_string() // Casts to non-empty string
# Input will always be an int

# If the int isn't in the database, None is always returned
def test_valdrug0():
    assert utility.valid_drug(0) == None 
def test_valdrug1():
    assert utility.valid_drug(-43253) == None 
def test_valdrug2():
    assert utility.valid_drug(34323453245) == None 
    

def test_valdrug3():
    test_data = utility.valid_drug(445544)
    assert test_data['drug_name'] == 'URANIUM-235'
    assert test_data['din'] == 445544
    assert test_data['usage'] == 'Used to inflict a lethal dose of ionizing radiation.'
    assert test_data['dosage'] == 'Rub over chest for 15 minutes daily'
    assert test_data['quantity'] == 3

def test_valdrug4():
    assert utility.valid_drug(-445544) == None 

