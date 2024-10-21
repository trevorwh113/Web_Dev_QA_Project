import pytest

def inc(x):
    return x + 1


def test_answer_1():
    assert inc(4) == 5

def test_answer_2():
    assert inc(4) == 5

def test_answer_3():
    assert inc(4) == 5

def test_answer_4():
    assert inc(4) == 5

# """
# What I have to test:
# Middle and backend
# - Unit test for get_all_clients()
# - Unit test for filter_clients()
# - Unit test for get_all_inv()
# - Unit test for filter_inv()
# - Unit test for valid_string()
# - Unit test for valid_int()
# 
# More frontend focused
# - Functional test for ClientLookup (see A1)   // Relates to filter_clients()
# - Functional test for DrugLookup (see A1)     // Relates to filter_inv()
# - Functional test for naviguating to client lookup page
# - Functional test for naviguating to inventory search page
# - Maybe the ViewDrugInfo page too..."""