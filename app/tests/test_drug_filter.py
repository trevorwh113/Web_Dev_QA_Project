"""
This file contains unit tests for the drug_lookup feature,
using a mixture of decision partitioning (white-box), and
output partitioning (black-box).
"""
import pytest
import utility

# ------- INPUT FIXTURES -------
@pytest.fixture
def types():
    """Defines basic data types for comparisons."""
    return {"STR": type(""),
            "INT": type(0),
            "LST": type([])}

@pytest.fixture
def inventories():
    """Defines sample inventories used throughout test suite."""
    inv1 = [["a", 0, "b", "c", 1]]
    inv2 = [["a", 0, "b", "c", 1], ["ab", 0, "b", "c", 1]]
    return inv1, inv2


# ------- UNIT TESTING -------
# Success case for get_all_inv() ------------------------------
def test_get_all_inv(types):
    """
    Success case: get_all_inv() returns a non-empty 2d-list 
    matching: [[str, int, str, str, int], ...]
    """
    data = utility.get_all_inv()
    # Check the outside list.
    assert type(data) == types["LST"], "Return value should be a list"
    assert len(data) > 0, "Return value should be non-empty"
    # Check the inside list.
    entry = data[0]
    assert type(entry) == types["LST"], "Entry values should be lists"
    assert len(entry) == 5, "Entry values should have 5 elements"
    # Check the values of the inside list.
    assert type(entry[0]) == types["STR"], "drug_name should be a string"
    assert type(entry[1]) == types["INT"], "DIN should be an integer"
    assert type(entry[2]) == types["STR"], "usage should be a string"
    assert type(entry[3]) == types["STR"], "dosage should be a string"
    assert type(entry[4]) == types["INT"], "quantity should be an integer"

# Success cases for filter_inv() ------------------------------
def test_filter_inv_1(inventories):
    """Success case: filter_inv() finds 1 entry by DIN"""
    assert utility.filter_inv(inventories[0], 0) == inventories[0], "Failed to find included DIN"

def test_filter_inv_2(inventories):
    """Success case: filter_inv() finds 0 entries by DIN"""
    assert utility.filter_inv(inventories[0], 1) == [], "Wrongly found excluded DIN"

def test_filter_inv_3(inventories):
    """Success case: filter_inv() finds 1 entry by valid drug_name"""
    assert utility.filter_inv(inventories[0], "a") == inventories[0], "Failed to find included drug name"

def test_filter_inv_4(inventories):
    """Success case: filter_inv() finds 0 entries by valid drug_name"""
    assert utility.filter_inv(inventories[0], "b") == [], "Wrongly found excluded drug name"

def test_filter_inv_5(inventories):
    """Success case: filter_inv() finds 0 entry by invalid DIN"""
    assert utility.filter_inv(inventories[0], "") == [], "Wrongly searched using invalid drug name"

def test_filter_inv_6(inventories):
    """Success case: filter_inv() finds 2 entires by valid drug_name"""
    assert utility.filter_inv(inventories[1], "a") == inventories[1], "Failed to find multiple entries with partial drug name"

# Failure cases for filter_inv() ------------------------------
def test_filter_inv_fail_1():
    """Failure case: filter_inv() throws TypeError if inv is not iterable."""
    try:
        utility.filter_inv(0, "a")
        assert False, "Did not throw TypeError for inv not iterable"
    except TypeError:
        assert True

def test_filter_inv_fail_2():
    """Failure case: filter_inv() throws TypeError if inv[entry] is not indexable"""
    try:
        utility.filter_inv([0], "a")
        assert False, "Did not throw TypeError for inv[entry] not indexable"
    except TypeError:
        assert True

def test_filter_inv_fail_3():
    """Failure case: filter_inv() throws IndexError if inv[entry][0] does not exist"""
    try:
        utility.filter_inv([[]], "a")
        assert False, "Did not throw IndexError for inv[entry][0] does not exist"
    except IndexError:
        assert True

def test_filter_inv_fail_4():
    """Failure case: filter_inv() throws AttributeError if inv[entry][0] is not a string"""
    try:
        utility.filter_inv([[0]], "a")
        assert False, "Did not throw AttributeError for inv[entry][0] not a string"
    except AttributeError:
        assert True

def test_filter_inv_fail_5():
    """Failure case: filter_inv() throws IndexError if inv[entry][1] does not exist"""
    try:
        utility.filter_inv([[0]], 0)
        assert False, "Did not throw IndexError for inv[entry][1] does not exist"
    except IndexError:
        assert True

