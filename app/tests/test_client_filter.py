"""
This file contains unit tests for the client_lookup feature,
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
def clients():
    """Defines sample clients used throughout test suite."""
    clients1 = [["john doe", "01/01/2004", "123-456-7890", 1]]
    clients2 = [["john smith", "01/01/2004", "123-456-7890", 1],["john smith", "31/12/2004", "098-765-4321", 2]]
    return clients1, clients2


# ------- UNIT TESTING -------
# Success case for get_all_clients() ------------------------------
def test_get_all_clients(types):
    """
    Success case: Tests that get_all_clients() returns a non-empty
    2d-list matching: [[str, str, str, int], ...]
    """
    data = utility.get_all_clients()
    # Check the ouside list.
    assert type(data) == types["LST"], "Return value should be a list"
    assert len(data) > 0, "Return value should be non-empty"
    # Check the inside list.
    entry = data[0]
    assert type(entry) == types["LST"], "Entry values should be lists"
    assert len(entry) == 6, "Entry values should have 6 elements"
    # Check the values ofthe inside list.
    assert type(entry[0]) == types["STR"], "full_name should be a string"
    assert type(entry[0]) == types["STR"], "full_name should be a string"
    assert type(entry[1]) == types["STR"], "birth_date should be a string"
    assert type(entry[2]) == types["STR"], "phone_number should be a string"
    assert type(entry[3]) == types["LIST"], "active_prescriptions should be an integer"
    assert type(entry[3]) == types["LIST"], "active_prescriptions should be an integer"

# Success cases for filter_clients() ------------------------------
def test_filter_clients_1(clients):
    """Success case: filter_clients() finds 1 entry by name"""
    assert utility.filter_clients(clients[0], "john doe") == clients[0], "Failed to find included name"

def test_filter_clients_2(clients):
    """Success case: filter_clients() finds 0 entries by name/phone"""
    assert utility.filter_clients(clients[0], "someone else") == [], "Wrongly found excluded name/phone"

def test_filter_clients_3(clients):
    """Success case: filter_clients() finds 1 entry by valid phone number"""
    assert utility.filter_clients(clients[0], "123-456-7890") == clients[0], "Failed to find included phone number"

def test_filter_clients_4(clients):
    """Success case: filter_clients() finds 0 entry by invalid name/phone"""
    assert utility.filter_clients(clients[0], "") == [], "Wrongly searched using invalid name/phone"

def test_filter_clients_5(clients):
    """Success case: filter_clients() finds 2 entires by valid name"""
    assert utility.filter_clients(clients[1], "john smith") == clients[1], "Failed to find multiple entries with name"

# Failure cases for filter_clients() ------------------------------
def test_filter_clients_fail_1():
    """Failure case: filter_clients() throws TypeError if clients is not iterable."""
    try:
        utility.filter_clients(0, "a")
        assert False, "Did not throw TypeError for clients not iterable"
    except TypeError:
        assert True

def test_filter_clients_fail_2():
    """Failure case: filter_clients() throws TypeError if clients[entry] is not indexable"""
    try:
        utility.filter_clients([1], "a")
        assert False, "Did not throw TypeError for clients[entry] not indexable"
    except TypeError:
        assert True

def test_filter_clients_fail_3():
    """Failure case: filter_clients() throws IndexError if clients[entry][0] does not exist"""
    try:
        utility.filter_clients([[]], "a")
        assert False, "Did not throw IndexError for clients[entry][0] does not exist"
    except IndexError:
        assert True

def test_filter_clients_fail_4():
    """Failure case: filter_clients() throws AttributeError if clients[entry][0] is not a string"""
    try:
        utility.filter_clients([[0]], "a")
        assert False, "Did not throw AttributeError for clients[entry][0] not a string"
    except AttributeError:
        assert True

def test_filter_clients_fail_5():
    """Failure case: filter_clients() throws IndexError if clients[entry][2] does not exist"""
    try:
        utility.filter_clients([["a","b"]], 0)
        assert False, "Did not throw IndexError for clients[entry][2] does not exist"
    except IndexError:
        assert True

