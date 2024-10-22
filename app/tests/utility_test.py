import utility, pytest
from client import Client
    
def test_existing_client():
    """
    GIVEN a client phone number
    WHEN the string is passed through to the function
    THEN the correct client is returned
    """
    c = utility.get_client_by_phone("(123)-456-7890")
    assert c != 0
    assert c.phone_number == "(123)-456-7890"
    assert c.first_name == "John"
    assert c.last_name == "Doe"
    assert c.dob == "28/09/2004"
    assert len(c.active_prescripts) == 5
    assert len(c.old_prescripts) == 1

def test_non_existant_client():
    """
    GIVEN a client phone number for a non-existant client
    WHEN the string is passed through to the function
    THEN 0 value is returned (indicating failure)
    """
    c = utility.get_client_by_phone("(333)-333-3333")
    assert c == 0
    
def test_second_existing_client():
    """
    GIVEN a client phone number
    WHEN the string is passed through to the function
    THEN the correct client is returned
    """
    c = utility.get_client_by_phone("(123)-767-5456")
    assert c != 0
    assert c.phone_number == "(123)-767-5456"
    assert c.first_name == "Helio"
    assert c.last_name == "Ptile"
    assert c.dob == "8/02/2000"
    assert len(c.active_prescripts) == 5
    assert len(c.old_prescripts) == 1