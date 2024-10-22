import utility, pytest
from client import Client
  

def setup_client():
    pass
    
def test_existing_client():
    
    c = utility.get_client_by_phone("(123)-456-7890")
    assert c != 0
    assert c.phone_number == "(123)-456-7890"
    assert c.first_name == "John"
    assert c.last_name == "Doe"
    assert c.dob == "28/09/2004"
    assert len(c.active_prescripts) == 5
    assert len(c.old_prescripts) == 1

def test_non_existin_client():
    c = utility.get_client_by_phone("(333)-333-3333")
    assert c == 0
    
def test_second_existing_client():

    c = utility.get_client_by_phone("(123)-767-5456")
    assert c != 0
    assert c.phone_number == "(123)-767-5456"
    assert c.first_name == "Helio"
    assert c.last_name == "Ptile"
    assert c.dob == "8/02/2000"
    assert len(c.active_prescripts) == 5
    assert len(c.old_prescripts) == 1

"""
What I have to test:

utility.py:
- get_active_prescripts()
- get_client_by_phone()
- should take a string formatted to (xxx)-xxx-xxxx
- can just strip and convert to each chara to int (count of 10)

client.py:
- init
- add new prescript
- add old prescript

client_info.js
- 

ViewPrescriptions (A1)
ChangePrescriptionStatus (A1)

- Functional test for naviguating to client info page


"""