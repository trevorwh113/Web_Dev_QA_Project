"""
Success and failure unit test cases for the get_client_by_phone()
backend-link function prodived in uility.py.
"""
import utility, pytest


def test_existing_client_1():
    """
    GIVEN a client phone number
    WHEN the string is passed through to the function
    THEN the correct client is returned
    """
    c = utility.get_client_by_phone("(123)-456-7890")
    assert c[0] == "(123)-456-7890"
    assert c[1] == "JOHN"
    assert c[2] == "DOE"
    assert c[3] == "28/09/2004"
    
def test__existing_client_2():
    """
    GIVEN a client phone number
    WHEN the string is passed through to the function
    THEN the correct client is returned
    """
    c = utility.get_client_by_phone("(123)-767-5456")
    assert c[0] == "(123)-767-5456"
    assert c[1] == "HELIO"
    assert c[2] == "PTILE"
    assert c[3] == "08/02/2000"